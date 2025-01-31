from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

def query_db(sql, params=()):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

# Initialize the database with schema and sample data
def init_db():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Department TEXT,
            Salary INTEGER,
            Hire_Date TEXT
        );
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Manager TEXT
        );
        INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES
            (1, 'Alice', 'Sales', 50000, '2021-01-15'),
            (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
            (3, 'Charlie', 'Marketing', 60000, '2022-03-20');
        INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES
            (1, 'Sales', 'Alice'),
            (2, 'Engineering', 'Bob'),
            (3, 'Marketing', 'Charlie');
    ''')
    conn.commit()
    conn.close()

init_db()

class UserQuery(BaseModel):
    query: str

@app.post("/query")
def handle_query(user_query: UserQuery):
    query = user_query.query.lower()
    doc = nlp(query)
    
    if "employees" in query and "department" in query:
        for ent in doc.ents:
            if ent.label_ == "ORG":
                sql = "SELECT Name FROM Employees WHERE Department = ?"
                results = query_db(sql, (ent.text,))
                return {"employees": [row[0] for row in results]}
    
    elif "manager" in query and "department" in query:
        for ent in doc.ents:
            if ent.label_ == "ORG":
                sql = "SELECT Manager FROM Departments WHERE Name = ?"
                results = query_db(sql, (ent.text,))
                return {"manager": results[0][0] if results else "Not found"}
    
    elif "hired after" in query:
        for ent in doc.ents:
            if ent.label_ == "DATE":
                sql = "SELECT Name FROM Employees WHERE Hire_Date > ?"
                results = query_db(sql, (ent.text,))
                return {"employees": [row[0] for row in results]}
    
    elif "total salary expense for" in query:
        for ent in doc.ents:
            if ent.label_ == "ORG":
                sql = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
                results = query_db(sql, (ent.text,))
                return {"total_salary": results[0][0] if results[0][0] else 0}
    
    return {"error": "Unsupported query"}

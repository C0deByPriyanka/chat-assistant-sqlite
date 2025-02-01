from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3
import re
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import db_init

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

db_init.init_db()

def query_db(sql, params=()):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

known_departments = ["Sales", "Engineering", "Marketing"]

class UserQuery(BaseModel):
    query: str

@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query")
def handle_query(user_query: UserQuery):
    query = user_query.query.lower()
    department = None
    date = None

    # Look for department names using simple keyword matching (case insensitive)
    for dept in known_departments:
        if dept.lower() in query:
            department = dept
            break
    # Look for dates using regex (e.g., after 2021-01-01, or before a certain date)
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    date_match = re.search(date_pattern, query)
    if date_match:
        date = date_match.group(0)
    
    if "employees" in query and "department" in query:
        if department:
            sql = "SELECT Name FROM Employees WHERE Department = ?"
            results = query_db(sql, (department,))
            return {"employees": [row[0] for row in results]}
        return {"error": "Please specify the correct department."}
                
    
    elif "manager" in query and "department" in query:
        
        if department:
            sql = "SELECT Manager FROM Departments WHERE Name = ?"
            results = query_db(sql, (department,))
            return {"manager": results[0][0] if results else "Not found"}
        return {"error": "Please specify the correct department."}
    
    elif "hired after" in query:
        if date:
            sql = "SELECT Name FROM Employees WHERE Hire_Date > ?"
            results = query_db(sql, (date,))
            return {"employees": [row[0] for row in results]}
        return {"error": "Please specify correct date"}
    
    elif "total salary expense" in query:
        if department:
            sql = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
            results = query_db(sql, (department,))
            return {"total_salary": results[0][0] if results[0][0] else 0}
        return {"error": "Please specify the correct department."}
    
    return {"error": "Unsupported query"}

import sqlite3

def init_db():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    # Creating tables
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
    ''')

    # Inserting dummy data
    employees_data = [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
        (4, 'David', 'Sales', 55000, '2021-07-01'),
        (5, 'Eve', 'Engineering', 80000, '2019-04-25'),
        (6, 'Frank', 'Marketing', 62000, '2023-02-10'),
        (7, 'Grace', 'Engineering', 72000, '2021-11-30'),
        (8, 'Hannah', 'Sales', 48000, '2020-12-05'),
        (9, 'Ian', 'Marketing', 63000, '2022-08-15'),
        (10, 'Jack', 'Engineering', 76000, '2020-09-14')
    ]

    departments_data = [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie')
    ]

    # Insert data into Employees
    cursor.executemany(
        "INSERT OR IGNORE INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)",
        employees_data
    )

    # Insert data into Departments
    cursor.executemany(
        "INSERT OR IGNORE INTO Departments (ID, Name, Manager) VALUES (?, ?, ?)",
        departments_data
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

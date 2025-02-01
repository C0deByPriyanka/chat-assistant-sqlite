from utils import query_db, matches_pattern, parse_date, extract_department, query_patterns

def handle_query(query):
    department = extract_department(query)
    date = parse_date(query)

    if matches_pattern(query, query_patterns["employees_in_department"]):
        if department:
            sql = "SELECT Name FROM Employees WHERE Department = ?"
            results = query_db(sql, (department,))
            return {"employees": [row[0] for row in results]}
        return {"error": "Please specify the correct department."}

    elif matches_pattern(query, query_patterns["manager_of_department"]):
        if department:
            sql = "SELECT Manager FROM Departments WHERE Name = ?"
            results = query_db(sql, (department,))
            return {"manager": results[0][0] if results else "Not found"}
        return {"error": "Please specify the correct department."}

    elif matches_pattern(query, query_patterns["hired_after"]):
        if date:
            sql = "SELECT Name FROM Employees WHERE Hire_Date > ?"
            results = query_db(sql, (date,))
            return {"employees": [row[0] for row in results]}
        return {"error": "Please specify a correct date."}

    elif matches_pattern(query, query_patterns["total_salary_expense"]):
        if department:
            sql = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
            results = query_db(sql, (department,))
            return {"total_salary": results[0][0] if results[0][0] else 0}
        return {"error": "Please specify the correct department."}

    return {"error": "Unsupported query"}

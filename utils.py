import re
import sqlite3
from datetime import datetime

DB_NAME = "company.db"

# List of known departments
known_departments = ["Sales", "Engineering", "Marketing"]

# Query patterns
query_patterns = {
    "employees_in_department": [r"employees.*\b(in|from|of)\b.*department", r"who works in", r"list staff in"],
    "manager_of_department": [r"manager.*\bof\b.*department", r"who manages", r"head.*\bof\b.*department"],
    "hired_after": [r"hired.*after", r"joined.*after", r"employees.*post"],
    "total_salary_expense": [r"total salary.*\bof\b", r"salary expense", r"sum of salaries"]
}

# Execute SQL query
def query_db(sql, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

# Check if query matches a pattern
def matches_pattern(query, patterns):
    return any(re.search(p, query) for p in patterns)

# Extract & format dates from queries
def parse_date(query):
    date_patterns = [
        r'(\d{4}-\d{2}-\d{2})',      # YYYY-MM-DD
        r'(\d{2}/\d{2}/\d{4})',      # DD/MM/YYYY
        r'([A-Za-z]+ \d{1,2}, \d{4})' # Month Day, Year (e.g., Jan 15, 2023)
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, query)
        if match:
            date_str = match.group(0)
            try:
                if '-' in date_str:  
                    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                elif '/' in date_str:  
                    return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
                else:  
                    return datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                return None
    return None

# Extract department name
def extract_department(query):
    for dept in known_departments:
        if dept.lower() in query:
            return dept
    return None

employees = {
    "E001": {
        "name": "Fiona",
        "age": 29,
        "department": "HR"
    },
    "E002": {
        "name": "George",
        "age": 34,
        "department": "Engineering"
    }
}

# Print the department of employee E002
print(employees["E002"]['department'])  # Expected Output: "Engineering"


for emp_id, details in employees.items():
    print(f"ID: {emp_id}, Name: {details}, Department: {details}")
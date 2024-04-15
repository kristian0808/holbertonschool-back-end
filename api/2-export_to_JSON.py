#!/usr/bin/python3
"""
This script fetches todo tasks for a given employee id from the JSON
Placeholder API and exports them to a JSON file.

Usage:
    python3 2-export_to_JSON.py <employee_id>

Args:
    employee_id (int): The id of the employee whose tasks to fetch.

Examples:
    python3 2-export_to_JSON.py 1
"""

import requests
import sys
import json

if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

response = requests.get(url)
todos = response.json()

employee_request = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
)
employee_name = employee_request.json()["username"]

todo_data = []
for todo in todos:
    todo_data.append(
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name,
        }
    )

json_data = {employee_id: todo_data}

with open("{}.json".format(employee_id), "w") as file:
    json.dump(json_data, file)

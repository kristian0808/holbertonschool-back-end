#!/usr/bin/python3
"""
This script fetches todo tasks for a given employee id from the JSON
Placeholder API and exports them to a CSV file.

Usage:
    python3 1-export_to_CSV.py <employee_id>

Args:
    employee_id (int): The id of the employee whose tasks to fetch.

Examples:
    python3 1-export_to_CSV.py 1

Output:
    The CSV file named <employee_id>.csv containing the following columns:
        - employee_id (int): The id of the employee.
        - employee_name (str): The username of the employee.
        - completed (bool): The completion status of the todo.
        - title (str): The title of the todo.
"""

import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

response = requests.get(url)
todos = response.json()

employee_request = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
)
employee_name = employee_request.json()["username"]

with open("{}.csv".format(employee_id), "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow(
            [employee_id, employee_name, todo["completed"], todo["title"]])

#!/usr/bin/python3

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 todo_progress.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

response = requests.get(url)
todos = response.json()

total_tasks = len(todos)
completed_tasks = [todo for todo in todos if todo["completed"]]

employee_request = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
)
employee_name = employee_request.json()["name"]

print(
    "Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks
    )
)

for task in completed_tasks:
    print("\t {}".format(task["title"]))

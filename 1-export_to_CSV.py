#!/usr/bin/python3

import requests
import sys
import csv

if len(sys.argv) != 2:
    print("Usage: python3 todo_progress.py <employee_id>")
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
        writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

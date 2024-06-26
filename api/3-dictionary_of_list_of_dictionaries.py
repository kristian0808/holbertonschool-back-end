#!/usr/bin/python3
"""
This script fetches the list of users from the JSON Placeholder API
and creates a dictionary where each key is the user id and
each value is a list of dictionaries containing the user's username,
the task title and the completion status of each task.

The result is saved to a JSON file named todo_all_employees.json
"""

import json
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()

todo_all_employees = {}

for user in users:
    user_id = user["id"]
    username = user["username"]

    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_todos = []
    for todo in todos:
        user_todos.append(
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"],
            }
        )

    todo_all_employees[user_id] = user_todos

with open("todo_all_employees.json", "w") as file:
    json.dump(todo_all_employees, file, indent=4)

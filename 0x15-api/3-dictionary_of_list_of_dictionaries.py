#!/usr/bin/python3
"""
2-export_to_JSON.py

Task 2:
Exports the TODO list of an employee to a JSON file.

Requirements:
    - Records all tasks owned by the employee.
    - Format: { "USER_ID": [{
                    "task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS,
                    "username": "USERNAME"}, ... ]}
    - File name: USER_ID.json

Example:
    python3 2-export_to_JSON.py 2
    Creates a file named 2.json with the following content:
    {"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt",
        "completed": false,
        "username": "Antonette"}, ... ]}
"""
if __name__ == "__main__":
    from json import dump
    import requests

    url = 'https://jsonplaceholder.typicode.com'
    file_name = "todo_all_employees.json"
    # Get all users
    users_uri = "/users/"
    full_user_url = url + users_uri
    users_response = requests.get(full_user_url)
    users = users_response.json()
    # Get individual user tasks
    users_tasks = {}
    for user in users:
        # Get user info
        user_id = user.get("id")
        username = user.get("username")
        # Get tasks response
        task_uri = "/users/{}/todos".format(user_id)
        full_task_url = url + task_uri
        task_response = requests.get(full_task_url)
        tasks = task_response.json()
        # Enter user tasks into storage
        users_tasks[user_id] = []
        for task in tasks:
            data = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username}
            users_tasks[user_id].append(data)
    # Write data to JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        dump(users_tasks, file)

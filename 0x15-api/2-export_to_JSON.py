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
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    task_uri = "/users/{}/todos".format(employee_id)
    user_uri = "/users/{}".format(employee_id)
    full_task_url = url + task_uri
    full_user_url = url + user_uri
    file_name = "{}.json".format(employee_id)

    task_response = requests.get(full_task_url)
    user_response = requests.get(full_user_url)

    tasks = task_response.json()
    user = user_response.json()
    username = user.get("username")

    # Write data to JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        user_tasks = {employee_id: []}
        for task in tasks:
            data = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username}
            user_tasks[employee_id].append(data)
        dump(user_tasks, file)

        
        

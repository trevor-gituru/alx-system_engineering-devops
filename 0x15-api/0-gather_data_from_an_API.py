#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Task 0:
Fetches and displays the TODO list progress of an employee from a REST API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    task_uri = "/users/{}/todos".format(employee_id)
    user_uri = "/users/{}".format(employee_id)
    full_task_url = url + task_uri
    full_user_url = url + user_uri
    task_response = requests.get(full_task_url)
    user_response = requests.get(full_user_url)

    tasks = task_response.json()
    user = user_response.json()
    name = user.get("name")
    total_tasks = len(tasks)
    tasks_done = sum(1 for task in tasks if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total_tasks))
    for task in tasks:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))

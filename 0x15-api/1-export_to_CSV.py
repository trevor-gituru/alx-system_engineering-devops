#!/usr/bin/python3
"""
1-export_to_CSV.py

Task 1:
Exports the TODO list of an employee to a CSV file.

Requirements:
    - Records all tasks owned by the employee.
    - Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    - File name: USER_ID.csv

Example:
    python3 1-export_to_CSV.py 2
    Output file: 2.csv
    Content format:
    "2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
    ...
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    task_uri = "/users/{}/todos".format(employee_id)
    user_uri = "/users/{}".format(employee_id)
    full_task_url = url + task_uri
    full_user_url = url + user_uri
    file_name = "{}.csv".format(employee_id)

    task_response = requests.get(full_task_url)
    user_response = requests.get(full_user_url)

    tasks = task_response.json()
    user = user_response.json()
    username = user.get("username")

    # Write data to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            data = [employee_id, username,
                    task.get("completed"),
                    task.get("title")]
            writer.writerow(data)

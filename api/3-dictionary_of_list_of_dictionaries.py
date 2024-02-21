#!/usr/bin/python3
"""Script that gets user data (Todo list) from API
and then export the result to csv file. """

import json
import requests


def main():
    """main function"""
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    response = requests.get(todo_url)

    output = {}

    for todo in response.json():
        user_id = todo.get('userId')
        if user_id not in output.keys():
            output[user_id] = []
            user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                user_id)
            user_name = requests.get(user_url).json().get('username')

        output[user_id].append(
            {
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

    with open("todo_all_employees.json", 'w') as file:
        json.dump(output, file)


if __name__ == '__main__':
    main()

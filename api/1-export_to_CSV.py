#!/usr/bin/python3
"""Script that gets user data (Todo list) from API
and then export the result to csv file. """

import csv
import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    file_content = []

    response = requests.get(todo_url)
    user_name = requests.get(user_url).json().get('username')

    for todo in response.json():
        if todo.get('userId') == user_id:
            file_content.append(
                [str(user_id),
                 user_name,
                 todo.get('completed'),
                 "{}".format(todo.get('title'))])

    print(file_content)
    file_name = "{}.csv".format(user_id)
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in file_content:
            for item in row:
                str(item)
            csv_writer.writerow(row)
        print('file written successfully')


if __name__ == "__main__":
    main()

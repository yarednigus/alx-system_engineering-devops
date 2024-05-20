#write a python script that, using this REST API:
# https://jsonplaceholder.typicode.com/

#a)employee ID
#b) information about his/her TODO list progress
#c) you must use urllib or requests module
# d) script must accept an integer as a parameter, which is the employee# ID
# e) display employeee TODO list progress in thes exact format:

#fist line : employee EMPLOYEE_NAME is done 
# with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
import requests
import sys

if __name__ = "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()

    params = {"userID": employee_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()


    

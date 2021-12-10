from application import salary
from application.db import people
from datetime import datetime

def greetings():
    print('Greeting')

if __name__ == '__main__':
    print(datetime.now())
    greetings()
    people.get_employees('Dani')
    salary.calculate_salary(30, 1000)
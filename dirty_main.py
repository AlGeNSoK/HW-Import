from application.salary import *
from application.db.people import *
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now().date())
    get_employees()
    print(datetime.now().date())
    calculate_salary()
# This module prints the database and will be used to check the correctness of your work,
# therefore, you should follow the instruction to the letter!!!
from persistence import *
if __name__ == '__main__':
    os.remove('moncafe.db')
    e = Employee(1, 'amit', 500, 90)
    repo.__init__()
    repo.create_tables()
    repo.Employees.insert(e)
# This module prints the database and will be used to check the correctness of your work,
# therefore, you should follow the instruction to the letter!!!
from persistence import *
if __name__ == '__main__':
    os.remove('moncafe.db')
    e = Employee(1, 'amit', 500, 90)
    s = Coffee_stand(2, 'Buliding90', 3)
    repo.__init__()
    repo.create_tables()
    repo.Employees.insert(e)
    repo.Coffee_stands.insert(s)
    conn = sqlite3.connect('moncafe.db')


def printall():
    print('Coffee stands')
    coffee_stands = repo.Coffee_stands.find_all
    print(coffee_stands)
    print('Employees')
    print(repo.Employees.find_all)
    print('Products')
    print(repo.Products.find_all)
    print('Suppliers')
    print(repo.Suppliers.find_all)


printall()
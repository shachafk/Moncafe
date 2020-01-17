# This module prints the database and will be used to check the correctness of your work,
# therefore, you should follow the instruction to the letter!!!
from persistence import *


def printall():
    print('Coffee stands')
    coffee_stands = Coffee_stands.find_all(repo.Coffee_stands)
    for stand in coffee_stands:
        stand = (stand.id, stand.location, stand.number_of_employees)
        print(stand)
    print('Employees')
    employees = Employees.find_all(repo.Employees)
    for employee in employees:
        employee = (employee.id, employee.name, employee.salary, employee.coffee_stand)
        print(employee)
    print('Products')
    products = Products.find_all(repo.Products)
    for product in products:
        product = (product.id, product.description, product.price, product.quantity)
        print(product)
    print('Suppliers')
    suppliers = Suppliers.find_all(repo.Suppliers)
    for supplier in suppliers:
        supplier = (supplier.id, supplier.name, supplier.contact_information)
        print(product)


if __name__ == '__main__':
    os.remove('moncafe.db')
    e = Employee(1, 'amit', 500, 90)
    s = Coffee_stand(2, 'Buliding90', 3)
    repo.__init__()
    repo.create_tables()
    repo.Employees.insert(e)
    repo.Coffee_stands.insert(s)
    printall()



# def employeereport():
#     emolyees = repo.Employees.find_all
#     for emolyee in emolyees:
#         print(emolyee.name + emolyee.salary + emolyee.coffee_stand)




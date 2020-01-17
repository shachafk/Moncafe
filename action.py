import sys
from persistence import *


def insertActivity(line):
    date = str((line[3]))
    a = Activitie(line[0], line[1], line[2], date)
    repo.Activities.insert(a)



def supplyArrival(line):
    insertActivity(line)

    # update the product supplier
    product_id = line[0]
    quantity = line[1]
    p = Product(product_id, '', 0, quantity)
    Products.update(repo.Products, p)


def loadToReport(emploeeid, product_id, quantity):
    e = Employees.find(repo.Employees, emploeeid)
    name = str(e.name)
    salary = e.salary
    coffestand = e.coffee_stand
    location = Coffee_stands.findLocation(repo.Coffee_stands, coffestand)
    product = Products.find(repo.Products, product_id)
    income = int(product.price) * int(quantity)
    i = EmployeeReports.findIncome(repo.EmployeeReports, name)
    er = EmployeeReport(name, salary, location, income+i)
    repo.EmployeeReports.insert(er)


def sale(line):
    product_id = line[0]
    quantity = line[1]
    emploeeid = line[2]
    date = line[3]
    q = Products.find(repo.Products, product_id)
    i = -int(quantity)
    y = int(q.quantity)
    # check if there is enough products for the activity
    if i <= y:
        u = Product(product_id, '', 0, y - i)
        insertActivity(line)
        Products.update(repo.Products, u)
        loadToReport(emploeeid, product_id, y-i)


def handleLine(line):
    i = line[1]
    if i > '0':
        supplyArrival(line)
    elif i < '0':
        sale(line)


def main(args):
    with open(args[1]) as inf:
        for line in inf:
            line = line.strip()
            line = [x.strip() for x in line.split(',')]
            handleLine(line)


if __name__ == '__main__':
    main(sys.argv)

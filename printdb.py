# This module prints the database and will be used to check the correctness of your work,
# therefore, you should follow the instruction to the letter!!!
from persistence import *


def printall():
    print('Activities')
    activites = Activities.find_all(repo.Activities)
    for activitie in activites:
        activitie = (activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date)
        print(activitie)
    print('Coffee stands')
    coffee_stands = Coffee_stands.find_all(repo.Coffee_stands)
    for stand in coffee_stands:
        stand = (stand.id, str(stand.location), stand.number_of_employees)
        print(stand)
    print('Employees')
    employees = Employees.find_all(repo.Employees)
    for employee in employees:
        employee = (employee.id, str(employee.name), employee.salary, employee.coffee_stand)
        print(employee)
    print('Products')
    products = Products.find_all(repo.Products)
    for product in products:
        product = (product.id, str(product.description), product.price, product.quantity)
        print(product)
    print('Suppliers')
    suppliers = Suppliers.find_all(repo.Suppliers)
    for supplier in suppliers:
        supplier = (supplier.id, str(supplier.name), str(supplier.contact_information))
        print(supplier)
    print
    print('Employees report')
    ereports = repo.getEmploeeReport()
    for ereport in ereports:
        if isinstance(ereport.income,int):
            income = int(ereport.income)
        else:
            income = float(ereport.income)
        ereport = (str(ereport.name), ereport.salary, str(ereport.location), income)
        print(ereport)
    activite = Activities.find_all(repo.Activities)
    if next(activite, None) is not None:
        print
        print('Activities')
        reports = repo.getActivitiesReport()
        for report in reports:
            report = (report.date, str(report.description), report.quantity, str(report.seller), str(report.supplier))
            print(report)


if __name__ == '__main__':
    printall()


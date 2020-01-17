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
        supplier = (supplier.id, str(supplier.name), supplier.contact_information)
        print(product)
    print('Employees report')
    ereports = EmployeeReports.find_all(repo.EmployeeReports)
    for ereport in ereports:
        ereport = (str(ereport.name), ereport.salary, str(ereport.location), float(ereport.income))
        print(ereport)
    print('Activities')
    reports = ActivitiesReport.find_all(repo.ActivitiesReport)
    for report in reports:
        report = (report.date, report.description, report.quantity, report.seller, str(report.supplier))
        print(report)




if __name__ == '__main__':
    printall()



# def employeereport():
#     emolyees = repo.Employees.find_all
#     for emolyee in emolyees:
#         print(emolyee.name + emolyee.salary + emolyee.coffee_stand)




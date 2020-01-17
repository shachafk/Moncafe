# file: persistence.py

import sqlite3
import atexit
import os


# Data Transfer Objects:
class Employee(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class EmployeeReport(object):
    def __init__(self, name, salary, location, income):
        self.name = name
        self.salary = salary
        self.location = location
        self.income = income


class Supplier(object):
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Product(object):
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


class Coffee_stand(object):
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


class activitiereport(object):
    def __init__(self, date, description, quantity, seller, supplier):
        self.date = date
        self.description = description
        self.quantity = quantity
        self.seller = seller
        self.supplier = supplier


# Data Access Objects:
# All of these are meant to be singletons
class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
               INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, id):
        c = self._conn.cursor()
        all = c.execute("""
        SELECT * FROM Employees WHERE id = ?
        """, [id])

        return Employee(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Employees
        """).fetchall()

        return (Employee(*row) for row in all)


class EmployeeReports:
    def __init__(self, conn):
        self._conn = conn

    def findIncome(self, name):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT income FROM EmployeeReports WHERE name = ?
            """, [name])
        if c.rowcount > 0:
            return int(*c.fetchone())
        else:
            return 0

    def insert(self, employeeReport):
        self._conn.execute("""
               INSERT OR REPLACE INTO EmployeeReports (name, salary, location, income) VALUES (?,?,?,?)
           """, [employeeReport.name, employeeReport.salary, employeeReport.location, employeeReport.income])


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name,contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Suppliers
        """).fetchall()

        return (Supplier(*row) for row in all)


class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?,?)
        """, [product.id, product.description, product.price, product.quantity])

    def finddes(self, id):
        c = self._conn.cursor()
        all = c.execute("""
        SELECT description FROM Products WHERE id = ?
        """, [id])
        return str(*c.fetchone)

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Products
        """).fetchall()

        return (Product(*row) for row in all)
    def update(self, product):
        self._conn.execute("""
        UPDATE Products SET quantity = ? WHERE id = ?
        """, [product.quantity, product.id])

    def find(self, id):
        c = self._conn.cursor()
        all = c.execute("""
        SELECT * FROM Products WHERE id = ?
        """, [id])

        return Product(*c.fetchone())


class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffeestand):
        self._conn.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffeestand.id, coffeestand.location, coffeestand.number_of_employees])

    def findLocation(self, id):
        c = self._conn.cursor()
        all = c.execute("""
        SELECT location FROM Coffee_stands WHERE id = ?
        """, [id])

        return str(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Coffee_stands
        """).fetchall()

        return (Coffee_stand(*row) for row in all)


class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activitie):
        self._conn.execute("""
            INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?,?)
        """, [activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT product_id, quantity, activator_id, date FROM Activities
        """).fetchall()

        return (Activitie(*row) for row in all)


class ActivitiesReport:
    def __init__(self, conn_):
        self._conn = conn_

    def insert(self, activitiereport):
        self._conn.execute("""
            INSERT INTO ActivitiesReport (date, description, quantity, seller, supplier) VALUES (?, ?, ?, ?, ?, ?)
        """, [activitiereport.date, activitiereport.description, activitiereport.quantity, activitiereport.seller, activitiereport.supplier])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
             SELECT date, description, seller, supplier FROM ActivitiesReport
         """).fetchall()

        return (activitiereport(*row) for row in all)


# The Repository


class _Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = Employees(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Products = Products(self._conn)
        self.Coffee_stands = Coffee_stands(self._conn)
        self.Activities = Activities(self._conn)
        self.EmployeeReports = EmployeeReports(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
          CREATE TABLE Employees (
              id    INT PRIMARY KEY,
              name  TEXT  NOT NULL,
              salary    REAL    NOT NULL,
              coffee_stand  INT,
               
              FOREIGN KEY(coffee_stand) REFERENCES Coffee_stands(id)
          );

          CREATE TABLE Suppliers (
              id    INT PRIMARY KEY,
              name  TEXT    NOT NULL,
              contact_information   TEXT
          );

          CREATE TABLE Products (
              id    INT   PRIMARY KEY,
              description   TEXT    NOT NULL,
              price REAL    NOT NULL,
              quantity  INT NOT NULL
          );
          
          CREATE TABLE Coffee_stands (
              id    INT PRIMARY KEY,
              location  TEXT    NOT NULL,
              number_of_employees   INT
          );
          CREATE TABLE Activities (
              product_id    INT REFERENCES  Product(id),
              quantity  INT NOT NULL,
              activator_id  INT NOT NULL,
              date  DATE    NOT NULL,
               
              FOREIGN KEY(product_id) REFERENCES Products(id)
          );
             CREATE TABLE EmployeeReports (
              name  TEXT PRIMARY KEY,
              salary  REAL NOT NULL,
              location  TEXT NOT NULL,
              income  INT    NOT NULL,
               
              FOREIGN KEY(name) REFERENCES Employees(name),
              FOREIGN KEY(salary) REFERENCES Employees(salary),
              FOREIGN KEY(location) REFERENCES Coffee_stands(location)
          );
          CREATE TABLE ActivitiesReport (
              date    INT REFERENCES  Activities(date),
              description   TEXT    NOT NULL,
              quantity  INT NOT NULL,
              seller   TEXT REFERENCES  Employees(name),
              supplier  TEXT REFERENCES  Suppliers(name),

               
              FOREIGN KEY(date) REFERENCES Activities(date),
              FOREIGN KEY(seller) REFERENCES Employees(name),
              FOREIGN KEY(supplier) REFERENCES Suppliers(name)
          );
        """)


# see code in previous version...

# the repository singleton
repo = _Repository()
atexit.register(repo.close)

# file: persistence.py

import sqlite3
import atexit






# Data Transfer Objects:
class Employee(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


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


# Data Access Objects:
# All of these are meant to be singletons
class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
               INSERT INTO Employee (id, name,salary,coffee_stand) VALUES (?, ?,?,?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    # def find(self, student_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, name FROM students WHERE id = ?
    #     """, [student_id])
    #
    #     return Student(*c.fetchone())


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name,contact_information) VALUES (?, ?,?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    # def find(self, num):
    #     c = self._conn.cursor()
    #     c.execute("""
    #             SELECT num,expected_output FROM assignments WHERE num = ?
    #         """, [num])
    #
    #     return Assignment(*c.fetchone())


class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price,quantity) VALUES (?, ?, ?,?)
        """, [product.id, product.description, product.price, product.quantity])

    # def find_all(self):
    #     c = self._conn.cursor()
    #     all = c.execute("""
    #         SELECT student_id, assignment_num, grade FROM grades
    #     """).fetchall()
    #
    #     return [Grade(*row) for row in all]


class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffeestand):
        self._conn.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffeestand.id, coffeestand.location, coffeestand.number_of_employees])

    # def find_all(self):
    #     c = self._conn.cursor()
    #     all = c.execute("""
    #         SELECT student_id, assignment_num, grade FROM grades
    #     """).fetchall()
    #
    #     return [Grade(*row) for row in all]


class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activitie):
        self._conn.execute("""
            INSERT INTO Activities (product_id, quantity, activator_id,date) VALUES (?, ?, ?)
        """, [activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date])

    # def find_all(self):
    #     c = self._conn.cursor()
    #     all = c.execute("""
    #         SELECT student_id, assignment_num, grade FROM grades
    #     """).fetchall()
    #
    #     return [Grade(*row) for row in all]


# The Repository


class _Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = Employees(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Products = Products(self._conn)
        self.Coffee_stands = Coffee_stands(self._conn)
        self.Activities = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
          CREATE TABLE students (
              id      INT         PRIMARY KEY,
              name    TEXT        NOT NULL
          );

          CREATE TABLE assignments (
              num                 INT     PRIMARY KEY,
              expected_output     TEXT    NOT NULL
          );

          CREATE TABLE grades (
              student_id      INT     NOT NULL,
              assignment_num  INT     NOT NULL,
              grade           INT     NOT NULL,

              FOREIGN KEY(student_id)     REFERENCES students(id),
              FOREIGN KEY(assignment_num) REFERENCES assignments(num),

              PRIMARY KEY (student_id, assignment_num)
          );
      """)


# see code in previous version...

# the repository singleton
repo = _Repository()
atexit.register(repo._close)

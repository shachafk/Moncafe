#   This module builds the database and inserts the initial data from the configuration file.
#   When run, it will be given a configuration file as an argument.
#   For example: python3 initiate.py config.txt
#   If the database file already exists remove it.
import sqlite3
import sys
from persistence import *


# will create a connection to a file base database stored in 'mydb.db' file
# if the file does not exist, it will be created


def insertEmploee(toInsert):
    e = Employee(toInsert[1], toInsert[2], toInsert[3], toInsert[4])
    repo.Employees.insert(e)


def insertSupplier(toInsert):
    s = Supplier(toInsert[1], toInsert[2], toInsert[3])
    repo.Suppliers.insert(s)


def insertProduct(toInsert):
    p = Product(toInsert[1], toInsert[2], toInsert[3],0)
    repo.Products.insert(p)


def insertCoffeeStand(toInsert):
    c = Coffee_stand(toInsert[1], toInsert[2], toInsert[3])
    repo.Coffee_stands.insert(c)


def insertActivity(toInsert):
    a = Activitie(toInsert[1], toInsert[2], toInsert[3], toInsert[4])
    repo.Activities.insert(a)


def handleLine(line):
    toInsert = [x.strip() for x in line.split(',')]
    if toInsert[0] == 'E':
        insertEmploee(toInsert)
    elif toInsert[0] == 'S':
        insertSupplier(toInsert)
    elif toInsert[0] == 'P':
        insertProduct(toInsert)
    elif toInsert[0] == 'C':
        insertCoffeeStand(toInsert)
    elif toInsert[0] == 'A':
        insertActivity(toInsert)


def main(args):
    with open(args[1]) as inf:
        for line in inf:
            line = line.strip()
            handleLine(line)


if __name__ == '__main__':
    os.remove('moncafe.db')
    repo.__init__()
    repo.create_tables()
    main(sys.argv)

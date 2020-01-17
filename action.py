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


def sale(line):
    product_id = line[0]
    quantity = line[1]
    p = Product(product_id, '', 0, 0)
    q = Products.find(repo.Products, p)
    i = -int(quantity)
    y = int(q.quantity)
    # check if there is enough products for the activity
    if i <= y:
        u = Product(product_id, '', 0, y - i)
        insertActivity(line)
        Products.update(repo.Products, u)


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

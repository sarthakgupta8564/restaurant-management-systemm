import db as d
import products as prod

def insert(name,qty,price,sales):

    prod.insert(name,qty,price)
def display():
    prod.readall()




def update(name,qty,price):
    prod.update_item(name, qty, price)

def delete(name):

    prod.delete_item(name)







# File pizzashop.py (2.X + 3.X)
from __future__ import print_function
from employee import Server, Chef, PizzaRobot

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name,"pays for item to", server)

class Ovan:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.ovan = Ovan()
        self.server = Server('Pat')
        self.chef = Chef('bob')
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.ovan.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
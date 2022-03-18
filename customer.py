from re import T
from shopping_cart import ShoppingCart

class Customer:

    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def customer_add_product(self):
        self.shopping_cart.add_product

    def customer_products(self):
        for product in self.shopping_cart.products:
            print(product)

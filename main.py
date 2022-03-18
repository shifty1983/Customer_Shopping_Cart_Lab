from numpy import product
from customer import Customer
from product import Product

customer1 = Customer("Tony")

product1 = Product("apple", .5, "grocery")
product2 = Product("tire", 250, "auto")
product3 = Product("bicycle", 500, "recreation")

print(f"Customer's name is {customer1.name}")

customer1.customer_add_product(product1)
customer1.customer_add_product(product2)
customer1.customer_add_product(product3)

customer1.customer_products()

customer1_total = customer1.shopping_cart.sum_shopping_cart()

print(f" Customer's total is customer1_total")

customer1.shopping_cart.clear_shopping_cart()

customer1.customer_products()
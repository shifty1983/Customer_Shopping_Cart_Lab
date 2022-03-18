class ShoppingCart:

    def __init__(self):
        self.products = []

    def sum_shopping_cart(self):
        sum = 0
        for product in self.products:
            sum += product.price
        return sum

    def add_product(self, new_product):
        self.products.append(new_product)
    
    def clear_shopping_cart(self):
        del self.products[:]
        print("Cart has been emptied")

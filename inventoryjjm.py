from abc import ABC, abstractmethod


# Product Class (Base class)
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


# DigitalProduct Class (Derived from Product)
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size, download_link):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size
        self.download_link = download_link

    def get_product_info(self):
        base_info = super().get_product_info()
        return f"{base_info}, File Size: {self.file_size}MB, Download Link: {self.download_link}"


# PhysicalProduct Class (Derived from Product)
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight, dimensions, shipping_cost):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost

    def get_product_info(self):
        base_info = super().get_product_info()
        return f"{base_info}, Weight: {self.weight}kg, Dimensions: {self.dimensions}, Shipping Cost: {self.shipping_cost}"


# Discount Class (Abstract Base Class)
class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total_amount):
        pass


# PercentageDiscount Class (Derived from Discount)
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        return total_amount * (1 - self.percentage / 100)


# FixedAmountDiscount Class (Derived from Discount)
class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, total_amount):
        return total_amount - self.amount if total_amount - self.amount > 0 else 0


# Cart Class
class Cart:
    def __init__(self):
        self.__cart_items = []

    def add_product(self, product):
        self.__cart_items.append(product)

    def remove_product(self, product_id):
        self.__cart_items = [item for item in self.__cart_items if item.product_id != product_id]

    def view_cart(self):
        return [item.get_product_info() for item in self.__cart_items]

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.__cart_items)
        return total

    def apply_discount(self, discount: Discount):
        total = self.calculate_total()
        return discount.apply_discount(total)


# User Class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def remove_from_cart(self, product_id):
        self.cart.remove_product(product_id)

    def checkout(self, discount=None):
        total = self.cart.calculate_total()
        if discount:
            total = self.cart.apply_discount(discount)
        self.cart = Cart()  # Reset the cart after checkout
        return total

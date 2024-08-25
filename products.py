# products.py

class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid name, price, or quantity")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_current_quantity(self):
        return self.quantity

    def set_new_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate_product()

    def product_is_active(self):
        return self.active

    def activate_product(self):
        self.active = True

    def deactivate_product(self):
        self.active = False

    def show_product_details(self):
        details = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            details += f", Promotion: {self.promotion.name}"
        return details

    def set_promotion(self, promotion):
        self.promotion = promotion

    def product_purchased(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")
        if self.promotion:
            total_price_no_taxes = self.promotion.apply_promotion(self, quantity)
        else:
            total_price_no_taxes = self.price * quantity
        self.set_new_quantity(self.quantity - quantity)
        return total_price_no_taxes
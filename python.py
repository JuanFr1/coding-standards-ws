"""System that calculates the total price of items in a shopping cart"""


class Itemz:
    """The class that defines Itemz"""

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"

    def get_total(self):
        """Function that gets the total price"""
        return self.price * self.qty

    def get_environmental_fee(self):
        """Function that returns the environmental fee for electronics"""
        if self.category == "electronics":
            return 5 * self.qty
        return 0


class ShoppinCart:
    """The class that defines Shopping Cart"""

    def __init__(self):
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Function that adds items to the cart"""
        self.items.append(item)

    def calculate_subtotal(self):
        """Function that calculates the subtotal"""
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member):
        """Function that applies discounts"""
        if is_member:
            subtotal -= (subtotal * self.member_discount)
        if subtotal > 100:
            subtotal -= self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Function that calculates the total of the Shopping Cart"""
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)

        # Add environmental fees for electronics
        for item in self.items:
            subtotal += item.get_environmental_fee()

        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon.upper() == "YES":
            total -= (total * self.coupon_discount)

        return total


def main():
    """Main function that defines the program"""
    cart = ShoppinCart()

    item1 = Itemz("Apple", 1.5, 10)
    item2 = Itemz("Banana", 0.5, 5)
    item3 = Itemz("Laptop", 1000, 1)
    item3.category = "electronics"

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    is_member = True
    has_coupon = "YES"
    total = cart.calculate_total(is_member, has_coupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print("The total price is: $" + str(round(total, 2)))


if __name__ == "__main__":
    main()

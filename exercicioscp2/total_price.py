price = 180.5
quantity = 2
discount_percentage = 10.5


def calculate_total_price(price, quantity=1, discount_percentage=0):
    if discount_percentage:
        return (price * quantity) * (1 - (discount_percentage / 100))
    return price * quantity


print(calculate_total_price(price, 2, discount_percentage))
print(calculate_total_price(1000, discount_percentage=10))

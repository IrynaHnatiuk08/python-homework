def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною.")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Відсоток знижки має бути від 0 до 100")

    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    return final_price


assert calculate_discount(200.0, 15.0)
assert calculate_discount(100.0, 0.0) == 100.0
assert calculate_discount(50.0, 100.0) == 0.0

print(f"{calculate_discount(200.0, 15.0)} автотести пройшли успішно")

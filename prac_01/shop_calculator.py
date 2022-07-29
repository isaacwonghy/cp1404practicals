no_of_items = int(input("Number of items: "))
while no_of_items < 0:
    print("Invalid number of items!")
    no_of_items = int(input("Number of items: "))

price1 = float(input("Price of item: "))
price2 = float(input("Price of item: "))
price3 = float(input("Price of item: "))
total_price = price1 + price2 + price3
if total_price > 100:
    discount = total_price * 0.1
    total = total_price - discount
    print(f"Total price for 3 items is ${total:.2f}")

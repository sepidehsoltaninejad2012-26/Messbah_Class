#jam kol mabalegh az 1milion dolar bishtar nashavad.

sum_price = 0
product_list = []

while True:
    name = input("Enter Name: ")
    quantity = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))


product = {
    "name": name,
    "quantity": quantity,
    "price": price,
}
sum_price = sum_price + price * quanity
if sum_price <= 1000000:
    product_list.append(product)
else:
    print("price is not ok")
    break

for product in product_list:
    print(f'{product["name"]:10} by {product["quantity"]:20} ({poduct["price"]})')


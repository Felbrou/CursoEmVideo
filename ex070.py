# Python Exercise 070: Create a program that reads the name and price of various products.
# The program should ask whether the user will continue or not. At the end, show:
# A) what is the total spent on the purchase.
# B) how many products cost more than R$1000.
# C) what is the name of the cheapest product.
print('----' * 8)
print("      VERISSIMO IMPORTS")
print('----' * 8)
total_sum, product_higher, product_lower, c = 0, 0, 0, 0
product_lower_name = ''

while True:
    product_name = str(input("Product Name >> ")).strip()
    product_price = float(input("Price[U$] >> "))
    c += 1
    total_sum += product_price
    process = ' '
    while process not in 'YN':
        process = str(input("Continue?[Y/N] >>")).strip().upper()[0]
    print('----' * 6)
    if c == 1:
        product_lower = product_price
        product_lower_name = product_name.title()
    if product_price > 1000:
        product_higher += 1
    if product_price < product_lower:
        product_lower = product_price
        product_lower_name = product_name.title()
    if process == 'N':
        break

print(f"All purchase cost is \033[33m{total_sum:.2f}\033[m\nWe have \033[33m{product_higher}\033[m"
      f" product(s) that over cost U$1000.00\n"
      f"The lower price product is \033[34m{product_lower_name}\033[m that costs U$ \033[34m{product_lower:.2f}\033[m")
print('----------END OF PROGRAM----------')
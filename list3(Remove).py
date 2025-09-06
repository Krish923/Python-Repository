cart_items = []
num_items = int(input())

for i in range(num_items):
    item = input()
    cart_items.append(item)

remove_item = input()
if remove_item in cart_items:
    cart_items.remove(remove_item)

print("Cart contents:", cart_items)

grocery_list = ["apple", "bread", "milk", "eggs", "bananas"]

grocery_list.append("beans")
grocery_list.remove("bread")
grocery_list.sort()

print(" ")
print("Updated Grocery List:")

for item in grocery_list:
    print(item)

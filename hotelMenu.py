menu ={
    'Coffee':120,
    'Pizza':99,
    'Tea':49,
    'Burger':149,
    'Pasta':299,
    'Cold-Drink':25,
    'Salad':150,
    'Maggi':70
}

print("-----Welcome To Pizza Zone..-----")
print("Coffee: 120.00Rs\nPizza: 99.00Rs\nTea: 49.00Rs\nBurger: 149.00Rs\nPasta: 299.00Rs\nCold-Drink: 25.00Rs\nSalad: 150.00Rs\nMaggi: 70.00Rs")
print("------------------------")

order_total=0

item1 = input("Enter the name of the itmes you want to order... : ")

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} Has Been Added...")
else:
    print(f"Order items {item1} is not available in the menu!!!")

order_items = input("Do you want to another items ? (Yes/No) ")

if order_items == "Yes":
   item2 = input("Enter the name of the second itmes you want to order... : ")
   
   if item2 in menu:
       order_total += menu[item2]
       print(f"Your item {item2} Has Been Added...")
   else:
       print(f"Order items {item2} is not available in the menu!!!")

print(f"The total price is : {order_total}")

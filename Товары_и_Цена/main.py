fruits = {"Apple": 4.5, "Orange": 5.2, "Banana": 7.6, "Kiwi": 8.4}

for fruit, price in fruits.items():
    print(fruit,"-", price,"$")

cost = 0
while True:
    fruit = input("What ? (n - nothing)")
    if fruit == 'n':
        break
    qty = int(input("How many ?"))
    cost += fruits[fruit] * qty

print("Price: ", cost,"$")

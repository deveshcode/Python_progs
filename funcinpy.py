def food(item='chick'):
    if(item == "chick"):
        return 100

print("Enter the order")
f=input()
g=food()
print("The price of the item is ", g)
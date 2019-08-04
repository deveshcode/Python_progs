#in operator
animal = "bear"

list = ["cat","dog","wolf"]

list2 = [1,23,-234]

list.append("bear")
del list[0]

print(list)

list.append("cold")
list.append("warm")

list.sort()
print(list)

list.reverse()
print(list)

print(len(list))

for list in list:
    print(list)

print("the max and min are ",max(list2),"and",min(list2))
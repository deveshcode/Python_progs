list = ["cat","dog","wolf","owl","bear"]
list2 = [1,23,-234]
copy = list[:] + list2[:]
print(list[0:2])

for i in copy:
    print(i)
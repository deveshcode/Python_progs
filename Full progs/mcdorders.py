def order(item):
    if item==1:
        return 100
    elif item==2:
        return 50

flag=1
total=0

while flag==1:
    a=int(input("Here's your Menu :\n1.Chicken Burger\n2.Chicken Nugget\nPlease make a choice"))
    total=total+order(a)
    print("Current bill :",total,"")
    c=int(input("Continue Ordering ? (1/0)"))
    if(c==0):
        flag=0
        print("Here's your Final Bill to be Paid plus taxes:",total+total*0.05,"\nThank you for shopping with us !")

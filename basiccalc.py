print("Enter 2 numbers")
a=int(input())
b=int(input())
i=1
while i==1:
    print("Choose an Operation")
    print("1. Add 2. Substract 3. Multiply 4. Divide 5. Modulus 6. Exponent 7. Floor Division")
    c=int(input())
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)
    elif c==5:
        print(a%b)
    elif c==6:
        print(a**b)
    elif c==7:
        print(a//b)
    else:
        print("Please Select a Valid Operation")
    i=int(input("Continue ?(1/0)"))
    
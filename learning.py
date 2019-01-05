# A basic calculator app

while True:

    a = input("Enter a number")
    b = input("Enter another number")

    opt = input("Choose an operation\n1.Add\n2.Substract\n3.Multiply\n4.Divide\n5.Exit")
    if opt == "1":  # this is because by default it takes all to be string
        c = float(a) + float(b)
        print(c)
    elif opt == "2":
        c = float(a) - float(b)
        print(c)
    elif opt == "3":
        c = float(a) * float(b)
        print(c)
    elif opt == "4":
        c = float(a) // float(b)
        print(c)
    else:
        exit()


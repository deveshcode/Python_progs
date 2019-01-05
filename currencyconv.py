def convert(opt,cur):
    if(opt==1):
        cur=cur/70
        print("The converted is ",cur," dollars")
    if(opt==2):
        cur=cur*70
        print("The converted is ",cur," rupees")
    if(opt==3):
        cur=cur/80
        print("The converted is ",cur," Euros")
    if(opt==4):
        cur=cur*80
        print("The converted is ",cur," rupees")    

c=int(input("Choose a currency. \n1. Rupees to Dollar\n2. Dollars to Rupees\n3. Rupees to Euors\n4. Euros to Rupees\n"))
d=int(input("Enter the value to be converted"))
convert(c,d)        
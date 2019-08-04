f_name = input("Enter your first name")
m_name = input("Enter your middle name")
l_name = input("Enter your last name")
age = input("Enter your age")
hobby = input("Enter your hobby")
no_sib = int(input("Enter no. of sibling ( 0 if none )"))
sib = []
for i in range(no_sib):
    temp = input("Whats their name")
    sib.append(temp)

print("Alright heres somethings about yourself\n"
    "My name is ",f_name," ",m_name," ",l_name," and I am currently ",age," years old.\n I love doing ",hobby," in free time.\n I have ",no_sib," siblings")


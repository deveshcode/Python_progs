
# very basic use of if statement

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a  Tall Male")
elif is_male or is_tall:
    print("You are either a Tall person or a Male")
elif is_male and not is_tall:
    print("You are a short male")
else:
    print("You arent a Male")


# another example of if statement to find highest of 3 nos.

def maxof(a, b, c):
    if a >= b and a >= c:
        print("The Highest no. is" + str(a))
    elif b >= a and b >= c:
        print("The Highest no. is" + str(b))
    else:
        print("The Highest no. is" + str(c))


maxof(23, 45, 45)

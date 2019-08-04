# lets try a function with a parameter
def gen2(name, age):
    name = "wp"
    print(name)


a = "lol"
b = "gg"
gen2(a, b)

print(a)


# lets try a function which returns something

def cube(n):
    n = n * n * n
    return n


a = int(input("Enter a no."))
print(cube(a))

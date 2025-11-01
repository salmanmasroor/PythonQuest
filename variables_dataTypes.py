
#Swap Two numbers without using a temporary vaiable
a = 5
b = 10 
a = a + b
b = a - b
a = a - b

print(f"Swap: a={a} & b={b}")


# Check if a variable is an integer, float, or string and perform different operations based on the type.
x = "Python"

if isinstance(x, int):
    print(f"{x} is integer")
elif isinstance(x, float):
    print(f"{x} is float")
elif isinstance(x, str):
    print(f"{x} is String")
else:
    print("unknown")
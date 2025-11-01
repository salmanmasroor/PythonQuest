
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

# Convert a string containing a number to an integer and a float
data = "70"
integer = int(data)
print(integer, type(integer))
float_no = float(integer)
print(float_no , type(float_no))
#  Find the largest and smallest numbers in a list.
no_list = [12,23,43,12,34,12]
temp = 0
for number in no_list:
    if number > temp:
        temp = number
print(temp)

# Count the number of occurrences of a value in a list.
no_list = [12,23,43,12,34,12]
length = len(no_list)
check = []
count = 0
for i in range(length):
    count = 0
    if(no_list[i] in check):
        continue
    else:
        check.append(no_list[i])
    for j in range(length):
        if(no_list[i] == no_list[j]):
            count += 1
    print(no_list[i], "= ",count)


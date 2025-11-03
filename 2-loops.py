# loops

# Print all prime numbers between 1 and n
n = int(input("Enter the number: "))
for i in range(1,n + 1):
    count = 0
    for j in range(1,i + 1): # replace n wiht i
        if i % j == 0:
            count += 1
    
    if (count <= 2):
        print(i)

#  Print the Fibonacci sequence up to n terms
n = int(input("Enter the number: "))
a = 0
b = 1
print(a)
print(b)
for i in range(n-2):
    c  = a + b
    a = b
    b = c
    print(c)


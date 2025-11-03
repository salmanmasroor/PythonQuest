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
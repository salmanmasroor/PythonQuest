# loops

# Print all prime numbers between 1 and n
def prime_no(no: int) -> list:
    result = []
    for i in range(1,n + 1):
        count = 0
        for j in range(1,i + 1): # replace n wiht i
            if i % j == 0:
                count += 1
        
        if (count <= 2):
            result.append(i)
        
    return result

#  Print the Fibonacci sequence up to n terms
def fibonacci(n: int) -> list:
    a = 0
    b = 1
    result = [a,b]
    for i in range(n-2):
        c  = a + b
        a = b
        b = c
        result.append(c)
    return result

if __name__ == "__main__":
    
    n = int(input("Enter the number for iterate: "))
    print(prime_no(n))

    n = int(input("Enter the number for iterate for Fibonacci sequence: "))
    print(fibonacci(n))
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
    for _ in range(n-2): # i not in use then use _
        c  = a + b
        a = b
        b = c
        result.append(c)
    return result

def sum_digits(digit: int) -> int:
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit = digit // 10
    return sum

def reverse_list(no_list: list) -> list:
    start = 0
    end = len(no_list) - 1
    while start < end:
        temp = no_list[start]
        no_list[start] = no_list[end]
        no_list[end] = temp

        start += 1 
        end -= 1
    return no_list

if __name__ == "__main__":
    
    n = int(input("Enter the number for iterate: "))
    print(prime_no(n))

    n = int(input("Enter the number for iterate for Fibonacci sequence: "))
    print(fibonacci(n))

    n = int(input("Enter the digt for sum: "))
    print(sum_digits(n))

    a = [12,23,34,3,12]
    print(reverse_list(a))


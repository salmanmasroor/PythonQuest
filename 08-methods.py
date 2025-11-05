# Built in methods

# zip
names = ["Ali", "Sara", "Ahmed"]
scores = [90, 80, 85]

result = list(zip(names,scores))
print(result)

for name,score in zip(names,scores):
    print(name,"->",score)

# map 
list_values = ["100", "250", "90"]

converted = list(map(int, list_values))

print (converted)


# Square each number in a list using map() with a regular function.
def square(no: int):
    return no**2

numbers = [1, 2, 3, 4, 5]

result = list(map(square,numbers))

print(result)

# filter

numbers = [10, -5, 0, 23, -7, 3]
print(list(filter(lambda x : x>4,numbers)))

# Problem 2: Filter Valid Email Addresses

emails = ["alice@mail.com", "bob.com", "carol@gmail.com", "dave123"]

print(list(filter(lambda email: '@' in email,emails)))

# sort vs sorted

#sort
numbers = [4, 2, 7, 1]
numbers.sort()
print(numbers)  # [1, 2, 4, 7]

#sorted
numbers = [4, 2, 7, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 4, 7]
print(numbers)         # [4, 2, 7, 1] 



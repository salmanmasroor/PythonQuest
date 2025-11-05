# sets

# Create a set of 5 numbers
values = {1,2,3,4,5}
print(values, type(values))

#Add a new number to the set.
values.add(6)
print(values)

# Remove a specific number from the set
values.remove(2)
print(values)

# Check if a number exists in the set.

isexist = 4 in values
print(isexist)

# Find the length of the set.
print(len(values))

# Problem: Union of two sets
setA = {1,2,3,4,5}
setB = {4,5,3,1,2,6}
result = setA.union(setB)
print(result)

# other way
result = setA | setB
print(result)

# Find the intersection of two sets
result = setA.intersection(setB)
print(result)

# Find the difference between two sets.
result = setB.difference(setA)  # elements that perent in b not in A
print(result)

# Find the symmetric difference between two sets.

result = setA.symmetric_difference(setB) # elements that are present in either A or B, but not in both.
print(result)

#Check if one set is a subset of another.
result = setA.issubset(setB)
print(result)

#Remove duplicates from a list using a set.
list_no = [1,2,23,2,3,2,5,6,1,2]
remove_dup = list(set(list_no))
print(remove_dup)

# Find unique words in a sentence.
sentence = "I love Python and I love automation"
sentence = sentence.split(" ")
print(set(sentence))

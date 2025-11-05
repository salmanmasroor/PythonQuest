# Dictionary

#Create a dictionary named student to store a student’s name, age, and grade.

student = {
    "name" : "Ali",
    "age" : 20,
    "grade" : 3.7
}
print(student)

# Retrieve and print the value of the name key from the student dictionary.
print(student["name"])

# Add a new key email with a value for the student.
student["email"] = "exammple.@gmail.com"

print(student)

# Update the age key to a new value.

student["age"] = 21
print(student["age"])

# Remove the grade key from the student dictionary.

del student["grade"]
print(student)

# Check if the key email exists in the dictionary.
resposne = "email" in student.keys()
print(resposne)

# Check if the key phone exists in the dictionary.
resposne = "phone" in student
print(resposne)

#Print all keys of the student dictionary.
for key in student:
    print(key)

#Print all values of the student dictionary.
for value in student.values():
    print(value)

# Print all key-value pairs of the student dictionary.
for key,values in student.items():
    print(key,values)
    
#Count how many keys are in the dictionary.
print(len(student)) 
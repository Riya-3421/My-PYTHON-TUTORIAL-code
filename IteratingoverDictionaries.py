##Iterating over Dictionaries
# Iterating over keys in a dictionary
student = {"name": "Riya", "age": 22, "grade": "A"}
print(student)

for key in student.keys():
    print(key)

##Iterating over values
for value in student.values():
    print(value)

##Iterating over key value pairs
for key,value in student.items():
    print(f"{key}:{value}")

##Nested Dictionaries
student={
    "student1":{"name":"Krish","age":24},
    "student2":{"name":"Herica","age":35}
}
print(student)

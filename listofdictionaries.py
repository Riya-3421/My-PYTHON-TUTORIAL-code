##create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'.
##sort the list of dictionaries by the 'score' in descending order and print the sorted list.
students = [
    {'name':'Alice','score':78},
    {'name':'Riya','score':90},
    {'name':'Abhi','score':93},
    {'name':'David','score':65},
    {'name':'Charlie','score':79}
]
sorted_student=sorted(students,key=lambda x:x['score'],reverse=True)
print("sorted student by score in descending order:")
for student in "sorted_students":
    print(student)

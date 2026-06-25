##Keyword Arguments
##Define a function that takes three named arguments:
#first_name,last_name and age and returns a formatted string.Test the function with different inputs.
def format_person(first_name,last_name,age):
    return f"{first_name}{last_name} is {age} years old."

#Test
print(format_person(first_name="Riya",last_name="Gupta",age=22))
print(format_person(age=25,first_name="Prity",last_name="Kumari"))
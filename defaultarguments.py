##Default Arguments
##Define a function that takes two integers as input and returns their sum.
# The second integer should have a default value of 6.Test the function different inputs.
def add(x,y=6):
    return x+y
#Test
print(add(2))
print(add(10,20))
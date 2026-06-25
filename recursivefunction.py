##Recursive function
##Define a recursive function that calculates the factorial of a given number.
#Test the function with different inputs.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#Test
print(factorial(7))
print(factorial(9))
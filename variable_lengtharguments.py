##Define a function that takes a variable number of integer arguments and returns their product.
#Test the function with different inputs.
def multiply(*args):
    product=1
    for num in args:
        product*=num
    return product

#Test
print(multiply(4*3*8))
print(multiply(3*5*6*4))
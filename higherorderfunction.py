##Higher-order function
##Define a higher-order function that takes a function and a list of integers as arguments,
#and applies the function to each integer in the list.Test with different function at lists
def apply_function(func, lst):
    return [func(x)for x in lst]
#Test
print(apply_function(lambda x:x**2,[1,2,3,4,5]))
print(apply_function(lambda x:x+1,[1,2,3,4,5,]))
    
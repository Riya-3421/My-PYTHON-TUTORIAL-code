##Nested functions
def outer_function(x,y):
    def inner_function(a,b):
        return a*b
    return inner_function(x,y)

#Test
print(outer_function(3,8))
print(outer_function(12,5))
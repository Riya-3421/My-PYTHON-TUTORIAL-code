##Filter function
##Use the filter fuction to filter out all odd numbers from a list of integers.
#Test with different lists.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_number=list(filter(lambda x:x % 2==0,numbers))
print(even_number)
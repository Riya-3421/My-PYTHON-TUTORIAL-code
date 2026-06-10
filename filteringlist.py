##create a new list containing only the even numbers from the list created first positive integers using a list comprehension.
##print the new list.
list=list(range(1,21))
print(list)
evens=[x for x in list if x%2==0]
print(evens)
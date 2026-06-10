##Basic sets operation
##Adding and Removing Elements
my_set={1,2,3,4,5,6}
my_set.add(7)
print(my_set)
my_set.add(7)
print(my_set)

##Remove the elements from a set
my_set.remove(3)
print(my_set)
my_set.discard(11)
print(my_set)

##pop method
removed_element=my_set.pop()
print(removed_element)
print(my_set)

##clear all elements
my_set.clear()
print(my_set)

##set membership test
my_set={1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)




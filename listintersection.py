##Write a function that takes two lists and return a new list containing only the elements that are present in both lists.
##print the intersection list.
def list_intersection(lst1,lst2):
    return [x for x in lst1 if x in lst2]
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
intersection=list_intersection(list1,list2)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Intersection:{intersection}")



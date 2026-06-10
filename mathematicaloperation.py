##Mathematical operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
##Union
union_set=set1.union(set2)
print(union_set)

##Intersection
intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
#Difference
print(set1.difference(set2))
set1
set2.difference(set1)



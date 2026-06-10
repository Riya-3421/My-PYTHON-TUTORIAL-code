##create a nested tuple and iterate over the elements.printing each element.
nested_tpl=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
for tpl in nested_tpl:
    for elem in tpl:
        print(elem)
##To print the first three elements,the last elements,and the elements from index 2 to 5 of the tuple
## which we created first 10 positive integers. print the tuple.
tpl=tuple(range(1,11))
print(tpl)
print(f"first three elements:{tpl[:3]}")
print(f"last three element:{tpl[-3:]}")
print(f"elementd from index 2to5:{tpl[2:6]}")
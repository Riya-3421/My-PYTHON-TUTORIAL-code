##To print the first,middle and last elements of the tuple which we create the tuple with 10 positive integers.print the tuple.
tpl=tuple(range(1,11))
print(tpl)
print(f"first element:{tpl[0]}")
print(f"middle element:{tpl[len (tpl)//2]}")
print(f"last element:{tpl[-1]}")
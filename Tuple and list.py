##Create a tuple with the first 5 positive integers. Convert it to a list,append the number 6,and 
#convert it back to a tuple.Print the tuple.
tpl=(1,2,3,4,5)
lst=list(tpl)
lst.append(6)
tpl=tuple(lst)
print(tpl)

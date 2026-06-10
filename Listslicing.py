##create a list of the first 20 positive integers.print the list 
##and to print the five elements,the last five element and the elements from index 5 to 15 of the list in which we create.
lst=list(range(1,21))
print(lst)
print(f"first five elements:{lst[:5]}")
print(f"last five elements:{lst[-5:]}")
print(f"Elements from index 5 to 15:{lst[5:16]}")
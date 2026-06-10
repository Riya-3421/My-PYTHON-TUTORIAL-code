##Write a function that rotates a list by n positions.Print the Original and rotated list.
def rotate_list(lst,n):
    return lst[n:]+lst[:n]
Original_list=[1,2,3,4,5]
rotated_list=rotate_list(Original_list,2)
print(f"Original list:{Original_list}")
print(f"rotated list:{rotated_list}")
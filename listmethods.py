##create a list of random numbers and sort it in ascending and descending order.
##remove the duplicates from the list and print the modified list.
import random
random_numbers = [random.randint(1,20) for i in range(15)]
print(f"Original list:{random_numbers}")
sorted_numbers=sorted(random_numbers)
print(f"sorted in ascending order:{sorted_numbers}")
sorted_numbers_desc=sorted(random_numbers,reverse=True)
print(f"sorted in descending order:{sorted_numbers_desc}")
unique_numbers=list(set(random_numbers))
print(f"list with duplicates remoed:{unique_numbers}") 


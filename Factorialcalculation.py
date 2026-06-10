##WAP that calculates the factorial of a number input by the user using a While loop.
number=int(input("Enter a number:"))
factorial=1
i=1
while i<=number:
    factorial*=i
    i+1
    print(f"The factorail of {number} is {factorial}")
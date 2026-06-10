##To print the first n Fibonacci numbers where n is the number input by the user
n=int(input("Enter the number of the Fibonacci numbers to print:"))
a,b=0,1
count=0
while count<n:
    print(a)
    a,b=b,a+b
    count+=1
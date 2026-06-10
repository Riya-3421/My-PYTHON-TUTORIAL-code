##To calculate the sum of the digits of a number input by the user using a while loop
number=int(input("Enter a number"))
sum_of_digits=0
while number > 0:
  digit=number%10 
sum_of_digits+=digit
number=number//10
print(f"The sum of the digit is {sum_of_digits}")
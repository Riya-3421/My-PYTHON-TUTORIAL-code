##Dictionary comprehension
squares={x:x**2 for x in range(7)}
print(squares)

##Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)

# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the 
# even-valued terms.

a = 0 
b = 1
fib = 0 
sum = 0

for num in range(1, 33):
  # fibonacci algo
  fib = a + b 
  a = b
  b = fib
  
  # checks if value is even number
  if(fib % 2 == 0):
    sum += fib

print(sum)
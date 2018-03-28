# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.


sum_sq = 0
sum = 0

# computes for the sum of squares
for num in range(1,11):
  sum_sq += num ** 2 

# computes for the summation of the values in range
for num in range(1,11):
  sum += num

# square of the sum
sq_sum = sum ** 2

# difference between the sum of squares
# and square of the sum
diff = sq_sum - sum_sq

print(diff)


# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

num = 2 ** 15 # 2^15
mod = 0
sum = 0

while num != 0:
  # gets the last digit
  mod = num%10 
  
  # adds up
  sum += mod
  
  # "removes" the last digit
  num = num/10
  
print(sum)


# /////////////////// alternate approach /////////////////// 
# num = 2 ** 15
# num_str = str(num) # converts num into string
# sum = 0 
# a = 0 
#
# for i in range(len(num_str)):
#   a = num_str[i] # gets a character at a certain position
#   sum += int(a)  # converts back to int so that it can be summed
# 
# print(sum)
  
  
  
  
  

# Read an integer N.
# Without using any string methods, try to print the ff.:
# 123...N
# *Note that "..." represents the values in between.

n = int(input())
    
for x in range(1,n+1):
	print(x, end='')
# Author: David De la Mora
# Date: Oct 17, 2020

n = 100
# list 1, 2, 3.. n
for i in range(1, n+1):
  print i

# list 1, 3, 5,. n
for i in range(1, n+1, 2):
  print i

# list 2, 4, 6.. n
for i in range(2, n+1, 2):
  print i

# list 10, 20, 30.. n
for i in range(10, n+1, 10):
  print i

# list n, ... 3, 2, 1
for i in range(n, 0, -1):
  print i


# sum, average 1..n example

n = 5
sum=0

for i in range(1, n+1):
  print i
  sum += i

avg = sum/n	
print "sum 1..",n, sum
print "average : ",avg


# fact example

fact=1
n = 150
for i in range(1,n+1):
  print i
  fact *= i

print "n! = ", fact


# x^3 function

for i in range(-10, 11, 1):
  print i

print "\n fx \n"

for i in range(-10, 11, 1):
  fx = i*i*i
  print fx


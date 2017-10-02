# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 1

if x > 0:
  for y in range (1, 4):
    if x % y == 0 :
      print x
    else:
      x += 1
      break
  print x

# items = range(1, 3)
# a = len(items)

# while x < 11:
#   for

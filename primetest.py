def prime(a):
  b = a-1
  even = 0
  for x in range (2, b):
    if a % x == 0:
      even = False
      break
    else:
      even = True
  return even

if prime(13):
  print "Tak"
else:
  print "Nie"

prime(25)

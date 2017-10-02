# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fibbonaci(a, b, c):
  fibb = [a, b]
  for x in range(a, c):
    last = fibb[-1]
    plast = fibb[-2]
    if last + plast < 4000000:
      fibb.append(last+plast)
  return fibb

def even_fibbonaci(list):
  summ = 0
  for x in list:
    if x % 2 == 0:
      summ += x
  print summ


fibb = fibbonaci(1, 2, 90)
even_fibbonaci(fibb)
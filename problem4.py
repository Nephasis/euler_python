#!/usr/bin/env python
# -*- coding: utf-8 -*-
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

n = 0

for x in range (999, 100, -1):
  for y in range (999, 100, -1):
    z = x * y
    if z > n:
      s = str(z)
      if s == s[::-1]:
        n = z

print n

import numpy as np
import math

#BEGIN EXERCISE 1

def to_base_b_int(b, n):
  assert n >= 0 & n%1 == 0, "n must be a non-negative integer"
  baseList = []
  currPow = int(math.log(n, b))
  while n > 0 & currPow >= 0:
    x = n // b**currPow
    y = x*b**currPow
    baseList += [x]
    currPow -= 1
    n -= y
  return baseList
    
#PART A

print(to_base_b_int(5, 123))
print(to_base_b_int(5, 495))
print(to_base_b_int(5, 31415926))
#base 5 representations

print(to_base_b_int(7, 123))
print(to_base_b_int(7, 495))
print(to_base_b_int(7, 31415926))
#base 7 representations

#PART B

def to_base_b(b, n):
  baseList = []
  currPow = int(math.log(abs(n), b))
  while abs(n) > 0:
    x = n // b**currPow
    y = x*b**currPow
    baseList += [x]
    currPow -= 1
    n -= y
  return baseList

print(to_base_b(8, 1/2))
print(to_base_b(8, -2))

#END EXERCISE 1

#BEGIN EXERCISE 2

def to_base_b_frac(b, x):
  assert 0 <= x < 1, "x must be in the interval [0,1)"
  digList = []
  y = 0
  for i in range(1,9):
    for j in range(b):
      if (y+j)/b**i <= x < (y+j+1)/b**i:
        digList += [j]
        y += j
        y *= b
        break
  return digList

#PART A

print(to_base_b_frac(3, 1/4))
print(to_base_b_frac(3, 8/13))

#PART B

print(to_base_b_frac(4, 3/7))
print(to_base_b_frac(4, 19/21))

#PART C

print(to_base_b_frac(5, 1))
print(to_base_b_frac(5, 5/4))
print(to_base_b_frac(5, -1/2))

#END EXERCISE 2

#BEGIN EXERCISE 3

def to_base_b_alpha(b, alpha):
  assert alpha >= 0, "x must be non-negative"
  inInt = int(alpha)
  inFrac = alpha - inInt
  if inInt == 0:
    outInt = [0]
  else:
    outInt = to_base_b_int(b, inInt)
  if inFrac == 0:
    outFrac = [0]
  else:
    outFrac = to_base_b_frac(b, inFrac)
  print("Integer part: ", outInt)
  print("Fractional part: ", outFrac)

#PART A

to_base_b_alpha(8, 1/2)
to_base_b_alpha(8, 123)
to_base_b_alpha(8, 22/7)
to_base_b_alpha(8, 0)
to_base_b_alpha(8, 1)
to_base_b_alpha(8, 90/1)
to_base_b_alpha(8, 495/290)

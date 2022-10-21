import numpy as np
import sympy as sp
import math
from matplotlib import pyplot as plt
import random

#BEGIN EXERCISE 1

def a(n):
  assert n % 1 == 0 and n >= 0, "n must be a natural number"
  return math.sin(n) 

#Part A

x = np.linspace(0, 1000, 1001)
y = np.sin(x)
plt.plot(x, y)
plt.show()
#sin(n) has limit points for every real number in [-1,1]

#Part B

#sin(n) has input domain of the naturals including 0
#thus, sin(n) has an output range of [-1,1]
#This set is closed and bounded, thus it is compact
#Because sin(n) is a sequence on a compact set
#It must contain a limit point

#Part C

def subsequence_close_to_limit(a, L, E):
  assert E > 0, "Degree of Error must be positive"
  x = np.linspace(0, 10000, 10001)
  b = [] #subsequence
  indexList = []
  for i in range(len(x)):
    if abs(a(i) - L) < E:
      b += [a(i)]
      indexList += [i]
  y = a(x)
  plt.plot(x, y, color='g', marker='.', markersize=1, linewidth=0) #plot parent sequence
  plt.plot(indexList, b, color='r', marker='.', markersize=16, linewidth=0) #plot subsequence
  plt.show()
  return indexList

#Part D
  
testLimit = random.uniform(-1,1)
print(testLimit)
subsequence_close_to_limit(np.sin, testLimit, 10**-3)
#Some real numbers do not show up as limit points in the first 10000 terms of sin(n)
#However, there is no discernable pattern between those that show and those that don't
#I still conject that sin(n) has limit points for all reals in [-1,1]

#END EXERCISE 1

#BEGIN EXERCISE 2

def a(n):
  assert n % 1 == 0 and n >= 0, "n must be a natural number"
  return math.sin(math.pi*n / 20)

#Part A

x = np.linspace(0, 1000, 1001)
y = np.sin(math.pi*x / 20)
plt.plot(x, y, 'r.')
plt.show()
#The set of limit points, L, of sin(pi*n / 20) is
#L = {x = sin(pi*n / 20 : n is an integer in [0,20]}

#Part B

#sin(pi*n / 20) has an input domain of the naturals including 0
#thus, sin(pi*n / 20) has an output range, r, such that,
#r is a subset of [-1,1],
#thus r is bounded,
#we can find that r = {x = sin(pi*n / 20 : n is an integer in [0,20]}
#proving r is finite
#and all finite subsets of R are closed
#thus r is compact
#and sin(pi*n / 20) is a sequence on a compact set
#It must contain a limit point

#Part C

testLimit = np.sin(np.pi*random.randint(0,20))
print(testLimit)
a = lambda n : np.sin(np.pi*n / 20)
subsequence_close_to_limit(a, testLimit, 10**-3)

#END EXERCISE 2

#BEGIN EXERCISE 3

def GCD(a,b):
  assert a % 1 == 0, "a must be n integer"
  assert b % 1 == 0 and b != 0, "b must be a non-zero integer"
  r = a % b
  if r == 0:
    return b
  else:
    return GCD(b,r)

#Part A

def enumerate_rationals(n):
  assert n % 1 == 0 and n >= 1, "n must be a natural number"
  ratList = [sp.Rational(0,1)]
  for i in range(1,n+1):
    for j in range(1, i+1):
      if GCD(i,j) == 1:
        ratList += [sp.Rational(j,i)]
  return ratList

#Part B

#SubPart a

y = enumerate_rationals(100)
x = np.linspace(0, len(y), y+1)
plt.plot(x, y, 'r.')
plt.show()
#I conject that the set of limits points of this sequence, L, is
#L = [0,1]

order_list = enumerate_rationals(1000)
def rational_index(x):
  if type(x) == int:
    return order_list[x]
  else:
    y = []
    for i in range(len(x)):
      y += [order_list[i]]
    return y

#SubPart b

#This sequence is a sequence on the set, r, of rationals in [0,1]
#r is bounded but not closed and thus is not compact
#However, this set is also infinite, therefore,
#The rationals are a subset of all limit points of the sequence, L
#However, if L only contained rationals, r would be closed,
#And thus we proved L contains all the irrationals in [0,1] as well

#SubPart c

testLimit = random.uniform(0,1)
print(testLimit)
subsequence_close_to_limit(rational_index, testLimit, 10**-3)
#by the same reasoning as the first exercise,
#I hold my conjecture that the set of limit points, L, of this sequence is
#L = [0,1]

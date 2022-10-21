import math
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

#BEGIN EXERCISE 1

X = sp.symbols('X')
f = lambda X : X**2 - 1

#f0 = x, f1 = x**2 - 1, f2 = x**4 - 2*x**2, f3 = x**8 - 4*x**6 + 4*x**4 - 1
#f0(0) = 0, f1(0) = -1, f2(0) = 0, f3(0) = -1
#f0(1) = 1, f1(1) = 0, f2(1) = -1, f3(1) = 0

#END EXERCISE 1

#BEGIN EXERCISE 2

def fnplot(x, show=True):
  xrange = np.linspace(0,50,51)
  yrange = [x]
  for i in range(1,len(xrange)):
    yrange += [f(yrange[i-1])]
  plt.plot(xrange,yrange, '.')
  if show == True:
    plt.show()

#END EXERCISE 2

#BEGIN EXERCISE 3

inputVals = np.linspace(1.1,1.7,7)
for n in inputVals:
  fnplot(n)
#Each value tested appears to regress into an alternating series,
#Except 1.7, whose values are not within the range of computability

#END EXERCISE 3

#BEGIN EXERCISE 4

P = (1 + 5**0.5) / 2
fnplot(P)
#I conject that the highest value of x, for which fn is bounded is
#x = (1 + math.sqrt(5)) / 2, which is the golden ratio

#END EXERCISE 4

#BEGIN EXERCISE 5

fnplot(-P)
#Similarly i conject that the lowest value of x, for which fn is bounded is
#x = -(1 + math.sqrt(5)) / 2, the negative golden ratio

#END EXERCISE 5

#BEGIN EXERCISE 6

p = 1/P
fnplot(P)
fnplot(p)
fnplot(-p)
fnplot(-P)
#The fixed points are when x equals, 
#(1 + math.sqrt(5)) / 2 and -2/(1 + math.sqrt(5))
#The negatives of these are almost fixed points but,
#their first terms differ from their proceeding terms

#END EXERCISE 6

#BEGIN EXERCISE 7

#The sequence appears to converge whenever your starting point is,
#Contained within a closed region of the Julia Set
#It interesting to note that,
#There are no closed regions in the corresponding Julia Set when,
#You begin with a point outside the Mandelbrot Set.

#END EXERCISE 7


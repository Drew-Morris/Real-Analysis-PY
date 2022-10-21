import os
import sys

import numpy as np

from matplotlib import pyplot as plt

import math

sys.setrecursionlimit(10000)

N = 20 #number of terms generated
a = [] #the empty list we will populate

for n in range(0,N):
  a.append(((-1.0)**n)*n/(2.0*n+1.0)) #populates a W 1st 20 terms of a_n
plt.plot(a,".") #"." == plot discrete points
plt.show() #displays the plot

#BEGIN EXERCISE 1
N = 50
a = []

for n in range(0,N):
  a.append(n/math.sqrt(n**2+1))
plt.plot(a,".")
plt.show() #The sequence appears to covnerge to 1
#END EXERCISE 1

N = 20
a = []

for n in range(0,N):
  a.append(((-1.0)**n)*n/(2.0*n+1.0))

plt.title("a plot of $a_n$") #title the plot
plt.xlim([-1,20]) #sets the x range to [-1,20]
plt.ylim([-1,1]) #sets the y range to [-1,1]
plt.plot(a,"mo") #sets marker to magenta circles
plt.show()

N = 20
a = [((-1.0)**n)*n/(2.0*n+1.0) for n in range(0,N)] #generates a from 0 to 20

plt.plot(a,".")
plt.show()

#BEGIN EXERCISE 2

#Part A
N = 21
b = []
for i in range(1,N+1):
  b.append((1-(i**(-1)))**i)

plt.plot(b,'yo')
plt.title("a plot of $(1-(1/n))^n$")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim([1,20]) 
plt.ylim([0,1])
plt.show()

#Part B
def f(x):
  return (1-(x**(-1)))**x

y = np.linspace(1,20,100)

plt.plot(y, f(y), 'c')
plt.title("a plot of $f(x) = (1-(1/x)^x$")
plt.xlim([0,20])
plt.ylim([0,1])
plt.show()

#You can denote the differences in the plots by titling them differently
#i.e. The sequence plot is titled "Sequence" and the function plot, "Function"

#END EXERCISE 2

#BEGIN EXERCISE 3

def fib(x): #Function for computing fibonacci numbers recursively
  if x <= 0:
    raise ValueError("n is not positive") 
  if x%1 != 0:
    raise ValueError("n is not an integer")
  else:
    if x == 1:
      return 1
    if x == 2:
      return 1
    else:
      return fib(x-1)+fib(x-2)

r = [] #fibonacci ratio list
for i in range(2,21):
  r.append((fib(i))/(fib(i-1)))

phi = ((1+math.sqrt(5))/2)

#I conjecture that the limit of r will be phi

def P(x):
  y = []
  for i in range(len(x)):
    y.append(phi)
  return y

x1 = np.linspace(0,21,100)

plt.plot(r,'mo')
plt.plot(x1, P(x1), 'c--')
plt.title("The Fibonacci Sequence and The Golden Ratio")
plt.show()

E = [] #extended fibonacci ratio list
for i in range(2,32):
  E.append((fib(i))/(fib(i-1)))

x2 = np.linspace(0,31,100)

plt.plot(E,'mo')
plt.plot(x2, P(x2), 'c--')
plt.title("The Fibonacci Sequence and The Golden Ration Ext.")
plt.show()

#The extended plot only further proves my conjecture

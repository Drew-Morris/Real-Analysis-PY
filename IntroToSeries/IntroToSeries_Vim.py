import numpy as np
from matplotlib import pyplot as plt
import math

#BEGIN EXERCISE 1

def seq1(n):
  return 1 / (2**n)

def ser1(N):
  sumPartial = 0
  for n in range(N):
    sumPartial += seq1(n)
  return sumPartial

def ser1print(N):
  for p in range(N):
    print(ser1(p))
  return 0

def ser1plot(N):
  x = np. linspace(0,N-1,num=N)
  y = []
  for s in range(N):
    y += [ser1(s)]
  plt.plot(x,y, 'o')
  plt.show()

#the series does appear to converge to 2

#END EXERCISE 1

#BEGIN EXERCISE 2

def seq2(n):
  return (-1)**n

def ser2(N):
  sumPartial = 0
  for n in range(N):
    sumPartial += seq2(n)
  return sumPartial

def ser2print(N):
  for p in range(N):
    print(ser2(p))
  return

def ser2plot(N):
  x = np.linspace(0,N-1,num=N)
  y = []
  for s in range(N):
    y += [ser2(s)]
  plt.plot(x,y, 'o')
  plt.show()
  return

#the series appears to alternate between 2 values, thus it diverges

#END EXERCISE 2

#BEGIN EXERCISE 3

def seq3(n):
  return 1/(n+1)

def ser3(N):
  sumPartial = 0
  for n in range(N):
    sumPartial += seq3(n)
  return sumPartial

def ser3print(N):
  for p in range(N):
    print(ser3(p))
  return

def ser3plot(N):
  x = np.linspace(0,N-1,num=N)
  y = []
  for s in range(N):
    y += [ser3(s)]
  plt.plot(x,y, 'o')
  plt.show()

#this series diverges

#END EXERCISE 3

#BEGIN EXERCISE 4

def seq4(n):
  return 1 / ((n+1) * math.log(n+2))

def ser4(N):
  sumPartial = 0
  for n in range(N):
    sumPartial += seq4(n)
  return sumPartial
  
def ser4print(N):
  for p in range(N):
    print(ser(p))
  return

def ser4plot(N):
  x = np.linspace(0, N-1, num=N)
  y = []
  for s in range(N):
    y += [ser4(s)]
  plt.plot(x,y)
  plt.show()
  return

#this series can be written as the product two series
#specifically the harmonic series and 1/(ln(n+1))
#the harmonic series is divergent
#so we only need to analyze the second series, which is visible divergent
#thus there product, this series, is divergent

#END EXERCISE 4

#BEGIN EXERCISE 5

def seq5(n):
  return (-1)**(n+2) * (math.floor(math.log2(n+2)) / (n+2))

def ser5(N):
  sumPartial = 0
  for n in range(N):
    sumPartial += seq5(n)
  return sumPartial

def ser5print(N):
  for p in range(N):
    print(ser5(p))
  return

def ser5plot(N):
  x = np.linspace(0,N-1,num=N)
  y = []
  for s in range(N):
    y += [ser5(s)]
  plt.plot(x,y, 'o')
  plt.show()
  return

#looking at this series plots it does appear to converge to 0; however,
#evaluating this series at higher and higher, N,
#we see it converges to a value just below 0

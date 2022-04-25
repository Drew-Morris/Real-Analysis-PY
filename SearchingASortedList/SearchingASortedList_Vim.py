import sympy as sp

from time import time

#BEGIN EXERCISE 1

def CubeRoot(K):
  i = 0
  #current iteration
  if K == 0:
    return 0
  if K < 0:
    return -1 * CubeRoot(-1 * K)
  else:
    if K == 1:
      return 1
    else:
      if K > 1:
        a = 1
        #lowerbound
        b = K
        #upperbound
      if K < 1:
        a = 0
        #lowerbound
        b = 1
        #upperbound
      while i <= 1000:
        m = (a + b) / 2
        #midpoint of a and b
        if i == 1000:
          return m
        else:
          i = i + 1
          if m**3 < K:
            a = m
            #if the midpoint cubed is less than K redefine a 
          if m**3 > K:
            b = m
            #if the midpoint cubed is more than K redefine b

#END EXERCISE 1

#BEGIN EXERCISE 2
            
def binary_search(L, n):
  min = 0
  max = len(L) - 1
  while max - min > 1:
    if L[min] == n:
      return min
    if L[max] == n:
      return max
    else:
      mid = int((min + max) / 2)
      if L[mid] < n:
        if min != mid:
          min = mid
      if L[mid] > n:
        if max != mid:
          max = mid
      if L[mid] == n:
        return mid
  return -1

#END EXERCISE 2

#BEGIN EXERCISE 3

def linear_search(L, n):
  for i in range(len(L)):
    if L[i] == n:
      return i
  return -1

def binary_search(L,n):
  list = sort(L)
  min = 0
  max = len(L) - 1
  while max - min > 1:
    if L[min] == n:
      return min
    if L[max] == n:
      return max
    else:
      mid = (min + max) / 2
      if L[math.floor(mid)] < n:
        min = math.floor(mid)
      if L[math.ceil(mid)] > n:
        max = math.ceil(mid)
  if L[min] == n:
    return min
  if L[max] == n:
    return max
  else:
    return -1

P = list(sp.primerange(1,1000000))

t = time()
print(binary_search(P, 823))
print("Time took: ", time() - t)
print(linear_search(P, 823))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 2))
print("Time took: ", time() - t)
print(linear_search(P, 2))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 191))
print("Time took: ", time() - t)
print(linear_search(P, 191))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 713))
print("Time took: ", time() - t)
print(linear_search(P, 713))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 1000))
print("Time took: ", time() - t)
print(linear_search(P, 1000))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 2))
print("Time took: ", time() - t)
print(linear_search(P, 2))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 9999991))
print("Time took: ", time() - t)
print(linear_search(P, 9999991))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 524287))
print("Time took: ", time() - t)
print(linear_search(P, 524287))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 1632913))
print("Time took: ", time() - t)
print(linear_search(P, 1632913))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 1234567))
print("Time took: ", time() - t)
print(linear_search(P, 1234567))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 10000000))
print("Time took: ", time() - t)
print(linear_search(P, 10000000))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 1))
print("Time took: ", time() - t)
print(linear_search(P, 1))
print("Time took: ", time() - t)

t = time()
print(binary_search(P, 512))
print("Time took: ", time() - t)
print(linear_search(P, 512))
print("Time took: ", time() - t)


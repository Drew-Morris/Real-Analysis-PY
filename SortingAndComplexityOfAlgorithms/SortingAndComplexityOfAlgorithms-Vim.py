#BEGIN EXERCISE 1

#Initial List
#[3,2,1,0]

#1st Pass
#[2,3,1,0]
#[2,1,3,0]
#[2,1,0,3]

#2nd Pass
#[1,2,0,3]
#[1,0,2,3]

#3rd Pass
#[0,1,2,3]

#This sorting method took 3 passes to succesfully sort the list
#I predict that the maximum number of passes to sort a set with length n
#Will be n-1 passes

#END EXERCISE 1

#BEGIN EXERCISE 2

def bubble_sort(l):
  for i in range(len(l)-1):
    term1 = l[i]
    term2 = l[i+1]
    if term1 > term2:
      l[i] = term2
      l[i+1] = term1
  for i in range(len(l)-1):
    if l[i] > l[i+1]:
      return bubble_sort(l)
  return l

#END EXERCISE 2

#BEGIN EXERCISE 3

l = [3,2,1,0]
print(l)
print(bubble_sort(l))

l = [10,9,8,7,6,5,4,3,2,1,0]
print(l)
print(bubble_sort(l))

l = [48, 81, 25, 12, 47, 4, 15, 90, 95, 7, 80, 68, 88, 8, 42, 3, 6, 14, 76, 19, 91, 52, 15, 51, 95, 1, 6, 81, 35, 99, 23, 24, 72, 94, 98, 88, 20, 84, 55, 32, 45, 99, 40, 51, 2, 25, 82, 66, 75, 30, 38, 8, 75, 33, 2, 7, 98, 61, 28, 2, 39, 100, 25, 89, 70, 41, 91, 8, 78, 61, 26, 9, 88, 92, 59, 44, 41, 60, 99, 80, 28, 53, 45, 95, 96, 84, 39, 55, 32, 98, 41, 23, 4, 14, 22, 4, 64, 12, 79, 43]
print(l)
print(bubble_sort(l))

#END EXERCISE 3

def my_sum_function(n):
  total = 0
  for i in range(n):
    total += i
  return total

def my_mult_funcion(n):
  prod = 1
  for i in range(1,n):
    for j in range(1,i):
      prod *= i+j
  return prod

def bad_factorial_funct(n):
  prod = 1
  for i in range(1,10):
    prod *= i
  return prod

#BEGIN EXERCISE 4

#The complexity of bubble sort is O((n-1)^2)

#Which means on average we are making ((n-1)^2) comparisons
#where n is the length of the input list

#There are two for loops

#END EXERCISE 4

#BEGIN EXERCISE 5

#The complexity of the binary search function is ceil(sqrt(n))
#where n is the length of the input list

#Starting with 16 we would make 4 cuts to find the element

#END EXERRCISE 5

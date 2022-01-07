# Write a Python Program to find sum of n natural numbers using recursion 

def recsum(n):
  if n <= 1:
       return n
  else:
      return n + recsum(n-1)
num = int(input())
if num < 0:
   print("Enter a positive number")
else:
   print(recsum(num))
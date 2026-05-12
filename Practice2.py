# Factorial Engineering: Write a program to find the factorial of a large integer using a for
# loop. Ensure you handle the case for 0! and negative inputs.
# a=int(input("enter "))
# am=1
# for i in range(1,a+1,1):
#     if a == 0:
#         print("1")
#     else:
#         am=am*i
# print(am)

# Divisor Discovery: Find all the factors (divisors) of a given number n and print them in
# ascending order.
# a=int(input("enter "))
# for i in range(1,a+1,1):
#     if a % i==0:
#         print(i)

# Primality Test: Check if a number is prime using a loop that iterates up to the square root
# of n for efficiency
# a = int(input("Enter number: "))
# prime = True
# for i in range(2, int(a**0.5) + 1):
#     if a % i == 0:
#         prime = False
#         break
# if a > 1 and prime:
#     print("Prime Number")
# else:
#     print("Not Prime")
# Fibonacci Sequence Generator: Generate the first n terms of the Fibonacci sequence
# where n is provided by the user.
# z = int(input("Enter number: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,z+1,1):
#     # print(i)
#     next=a+b
#     a=b
#     b=next
#     print(b)
#  Perfect Number Checker: A number is "perfect" if the sum of its proper divisors equals the
# number. Check if n is perfect.
# a = int(input("Enter number: "))
# sm=0
# for i in range(1,a,1):
#     if a % i == 0:
#         sm=sm+i
# print(sm)
# Strong Number: A Strong number is one where the sum of factorials of its digits equals the
# number itself. Determine if n is Strong.
# a = (input("Enter number: "))
# # am=1
# sm=0
# for i in a:
#     b=int(i)
#     am=1
#     for z in range(1,b+1,1):
#         am=am*z
#     sm=am+sm
#     # print(am)
# print(sm)
# a=int(a)
# if sm == a:
#     print(True)
# else:
#     print(False)
# Harmonic Series Sum: Calculate the sum of the series: 1 + 1/2 + 1/3 + ... + 1/n up to n terms
# n=int(input("enter "))
# sm=0
# for i in range(1,n+1,1):
#     # print(i)
#     sm=sm+1/i
#     print(sm)
# String Vowel Counter: Given a string, count the occurrences of each vowel using a loop
# and branching logic.
# a=input("Enter ")
# c=a.lower()
# b="a"
# d="e"
# e="i"
# f="o"
# g="u"
# s=0
# m=0
# l=0
# p=0
# q=0
# for i in c:
#     if i == b:
#         s=s+1
#     elif i == d:
#         m=m+1
#     elif i == f:
#         l=l+1
#     elif i == e:
#         p=p+1
#     elif i == g:
#         q=q+1
# print(b,":",s)
# print(d,":",m)
# print(f,":",l)
# print(e,":",p)
# print(g,":",q)
# Multiples within Range: Print all numbers between 1 and 500 that are divisible by both 7
# and 13.
# for i in range(1,501,1):
#     if i % 7 == 0 and i % 13 ==0:
#         print(i)
# Reverse a String: Iterate through a string from the last index to the first to create a
# reversed version.
# a="Python"
# sm=""
# for i in a[::-1]:
#     sm=sm+i
# print(sm)
# 11. Digit Product: Calculate the product of all digits of a given number, excluding any zeros.
# a=(input("Enter "))
# sm=1
# for i in a:
#     # print(i)
#     i=int(i)
#     if i!=0:
#         sm=sm*i
# print(sm)
# Prime Range: Print all prime numbers between two given integers [lower, upper].
# a=int(input("Enter "))
# b=int(input("Enter "))

# for i in range(a,b+1,1):
#     # print(i)
#     c=True
#     for z in range(2,i,1):
#         # print(z)
#         if i % z ==0:
#             c=False
#     if c == True:
#         print("prime",i)
# Power Function: Calculate x raised to the power of y (x^y) using a loop (Do not use ** or
# math.pow).
# x=int(input("Enter "))
# y=int(input("Enter "))
# sm=1
# for i in range(1,y+1,1):
#     sm=x*sm
# print(sm)  
#List Filtering: Given a list of integers, create a new list containing only those numbers
# whose sum of digits is even.
# a=(input("Enter "))
# a=a.split(",")
# z=[]
# for b in a:
#     f=b[0]
#     c=b[1]
#     d=int(f)
#     v=int(c)
#     m=d+v
#     print(m)
#     if m % 2==0:
#         z.append(int(b))
# print("Even Number",z)
# Consecutive Difference: Given a list, find the maximum difference between any two
# consecutive elements.
# a = [1, 7, 3, 10]
# sm = 0
# for i in range(len(a) - 1):
#     current = a[i]
#     next_value = a[i + 1]
#     diff = next_value - current
#     if diff > sm:
#         sm = diff
# print(sm)
# a=int(input("Enter "))
# sm="*"
# for i in a[::-1]:
#     sm=sm+i
#      print(sm)
# Common Elements: Given two lists, find their intersection using a loop and the 'in'
# operator.
# a=[1,2,3]
# b=[2,3,4]
# z=[]
# for i in a:
#     if i in b:
#         z.append(i)
# print(z)
# 18. Pascal's Triangle: Generate the first n rows of Pascal's triangle using nested loops.
# a = int(input("Enter rows: "))
# s = [1]
# for i in range(a):
#     print(s)
#     n = [1]
#     for z in range(len(s) - 1):
#         c = s[z] + s[z + 1]
#         n.append(c)
#     n.append(1)
#     s = n
# Collatz Sequence: For a given n, if n is even divide by 2, if odd multiply by 3 and add 1.
# Repeat until n=1. Track the number of steps.
# n=int(input("enter "))
# sm=0
# while n>1:
#     if n % 2==0:
#         n=n//2
#         sm=sm+1
#     elif n%2!=0:
#         n=n*3+1
#         sm=sm+1 
# print(sm)
#  Binary to Decimal: Convert a binary string into its decimal equivalent using a loop and
# powers of 2.
# a="1011"
# q=[]
# list=[]
# # list=[1,2,4,8]
# sm=0
# for i in a:
#       q.append(i)
# b=[int(x) for x in q]
# for e in range(len(b)):
#       list=2**e
#       s=b[e]*list
#       sm=sm+s
# print(sm)
# s=b[0]*list[0]
# v=b[1]*list[1]
# n=b[2]*list[2]
# m=b[3]*list[3]
# print(s+v+n+m)
# Pattern Generation (Diamond): Use nested for loops to print a diamond pattern of stars
# based on an odd number n (height).
# INPUT: n=5
# n = int(input("Enter odd number: "))
# space = n // 2
# for b in range(1, n + 1, 2):
#     print((" " * space) + ("*" * b))
#     space = space - 1
# space = 1
# for b in range(n - 2, 0, -2):
#     print((" " * space) + ("*" * b))
#     space = space + 1

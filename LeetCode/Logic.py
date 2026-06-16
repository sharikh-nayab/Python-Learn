# Take 2 numbers and print sum
# a = 2
# b = 3
# print(a+b)

# Swap 2 numbers (without temp)
# a=1
# b=6
# (a,b)=(b,a)   #Python internally creates a tuple (b, a)
# print(a,b)    #Then assigns values back → swapped in one line


#Check even/odd (use all 3 methods)
#Method- 1
# a=int(input("Please enter value= "))
# if a / 2:
#     print("Even")
# else:
#     print("Odd")
#Method 2
# a % 2 returns:
# 0 → when number is even
# 1 → when number is odd
# In Python:
# 0 → treated as False
# 1 → treated as True
# a=int(input("Please enter value= "))
# if a % 2:                                       
#     print("Odd")
# else:
#     print("Even")
#Method 3
# a=int(input("Please enter value= "))
# if a&2:
#     print("even")
# else:
#     print("Odd")
#Take name and print greeting
# a=(input("Please enter value= "))
# print(type(a), "Greetings")
#Check greater number between 2 inputs
# a=int(input("Please enter value= "))
# b=int(input("Please enter value= "))
# if a < b:
#     print(b," is greater than ",a)
# else:
#     print(a, "is greater than ", b)
#Check positive / negative / zero
# a=int(input("Please enter value= "))
# if a > 0:
#     print("Positive")
# elif a == 0:
#     print("Zero")
# else:
#     print("Negative")
#Find largest of 3 numbers
# a=int(input("Please enter value= "))
# b=int(input("Please enter value= "))
# c=int(input("Please enter value= "))
# if a > b >c:
#     print(a)
# elif a < b >c:
#     print(b)
# else:
#     print(c)
#Check divisible by 5 and 11
# a=int(input("Please enter value= "))
# if a %5==0 and a%11==0:
#     print("yes")
# else:
#     print("no")
#Sum of digits of a number
# a=(input("Please enter value= "))
# c=0
# for i in a:
#     #print(i)
#     b=int(i)
#     c=c+b
# print(c)
# b=a[0]
# c=a[1]
# d=int(b)
# e=int(c)
# print(d+e)
# Q3
# Q4
# Q1: Even or Odd using bitwise
# a=int(input("Type your number here= "))
# if a&1:
#     print("odd")
# else:
#     print("even")
# Q2: Take 2 numbers and print largest
# a=int(input("Type your number here= "))
# b=int(input("Type your number here= "))
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")
# Q3: Input: "10,20"
# Output: 30
# a=(input("Type your number here= "))
# b=a.split(",")
# print(b)
# for i in b:
#     c=int(b[0])
#     d=int(b[1])
#     f=c+d
# print(f)
# Q1: Take number and print:
# "Even and divisible by 4"
# "Even but not divisible by 4"
# "Odd"
# a=int(input("Type your number here= "))
# if a % 2==0 and a % 4 ==0:
#     print("Even and divisible by 4") 
# elif a % 2==0 and a % 4 !=0:
#     print("Even but not divisible by 4")
# else:
#     print("odd")
# Q2: Find greatest of 3 numbers without using max()
# a=(input("Type your number here= "))
# b=a.split(",")
# for i in b:
#     c=int(b[0])
#     d=int(b[1])
#     e=int(b[2])
# if c > d >e:
#     print("c")
# elif c < d > e:
#     print("d")
# else:
#     print("e")
# a=(input("Type your number here= "))
# b=a.split(",")
# #c=int(b)
# c=max(b)
# print(c)
# Q3: Reverse a number
# Input: 123
# Output: 321
# a=(input("Type your number here= "))
# b=a[::-1]
# print(b)
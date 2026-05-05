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
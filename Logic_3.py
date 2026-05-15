#Area of circle
# a=int(input("Please enter radius of circle= "))
# radius_of_circle = 3.14 * a * a
# print(radius_of_circle)
# Celsius to Fahrenheit
# a=int(input("Celcius = "))
# F = a * 9/5 + 32
# print(F)
# Swap two numbers
# a=10
# b=20
# # a,b = b,a
# temp=a
# a=b
# b=temp
# print(a,b)
# Find square of number
# a=int(input("Enter number= "))
# sq= a * a
# print(sq)
# Find cube of number
# a=int(input("Enter number= "))
# cu= a ** 3
# print(cu)
# Find simple interest
# a=int(input("Enter principle= "))
# b=int(input("Enter rate= "))
# c=int(input("Enter time= "))
# SI= a * b* c/100
# print(SI)
# Find average of 3 numbers
# a=int(input("Enter number= "))
# b=int(input("Enter number= "))
# c=int(input("Enter number= "))
# avg= a+b+c/3
# print(avg)
# Grade calculator
# a=int(input("Enter number= "))
# if a >= 90:
#     print("A")
# elif a >= 70:
#     print("B")
# elif a >= 50:
#     print("C")
# else:
#     print("Fail")
# for i in range(50):
#     if i % 2 ==0:
#         print("Even", i)
#     else:
#         print("Odd", i)
# Sum from 1 to n
# a=int(input("Enter number "))
# c=0
# for i in range(a):
#     c=c+i
# print(c)
# Multiplication table

# a=int(input("Enter value= "))
# for i in range(1,11,1):
#     b=i*a
#     print(b)
# Count numbers from 100 to 1
# for i in range(100,-1,1):
#     print(i)
# Given a 2D list (matrix), calculate the sum of elements in each row separately.
# Example:
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a :
#     sm=0
#     for z in i:
#         sm=sm+z
#     print(sm)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# sm=0
# zm=0
# ym=0
# for i in a:
#     sm=sm+i[0]
#     zm=zm+i[1]
#     ym=ym+i[2]
# print(sm)
# print(zm)
# print(ym)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# sm=0
# zm=0
# ym=0
# for i in a:
#     b=i[0]
#     c=i[1]
#     d=i[2]
#     sm=sm+b
#     zm=zm+c
#     ym=ym+d
# print(sm,zm,ym)
# Given a square matrix, calculate the sum of the main diagonal elements.
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# b=(a[0][0])
# c=(a[1][1])
# d=(a[2][2])
# print(b+c+d)
# sm=0
# for i in range(len(a)):
#     b=a[i][i]
#     sm=sm+b
# print(sm)
a=[[1,2,3],
 [4,5,6],
 [7,8,9]]
# b=a[0][2]
# c=a[1][1]
# d=a[2][0]
# print(b+c+d)
# sm=0
# for i in range(len(a)):
#     b=a[i][2-i]
#     sm=sm+b
# print(sm)
# Fibonacci Triangle
# Print a triangle pattern where numbers follow the Fibonacci sequence.
# 1
# 1 1
# 2 3 5
# 8 13 21 34
# a=int(input("Enter "))
# s=0
# m=1
# # print(m)
# for i in range(1,a+1,1):
#     for z in range(i):
#         next=s+m
#         s=m
#         m=next
#         print(next, end=" ")
#     print()
# Spiral Matrix Traversal
# Given a matrix, print elements in spiral order.
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# b=a[0][0]
# c=a[0][1]
# d=a[0][2]
# r=a[1][2]
# t=a[2][2]
# y=a[2][1]
# u=a[2][0]
# o=a[1][0]
# p=a[1][1]
# print(b,c,d,r,t,y,u,o,p)
# a=int(input("Enter "))
# for i in range(1,a+1):
#     for z in range(1,i+1):
#         print(z, end=" ")
#     print()
# a=int(input("enter "))
# sm=0
# for i in range(1,a+1,1):
#     # print(i)
#     for z in range(0,i,1):
#         sm=sm+1
#         print(sm, end=" ")
#     print()
# a=input("Enter ")
# for i in range():
#     print(i)
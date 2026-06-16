#  Sum of First N Numbers
# n=5
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# Sum of First N Odd Numbers
# n=int(input("Enter value= "))
# sum=0
# for i in range(1,2*n+1,2):
#     if i % 2 !=0:
#         sum=sum+i
#         # continue
# print(sum)
# Sum of First N Even Numbers
# n=int(input("Enter "))
# sum=0
# for i in range(1,2*n+1,1):
#     if i % 2==0:
#         sum=sum+i
# print(sum)

# Divisible by 3 and 5
# for i in range(1,51,1):
#     if i%3==0 and i %5==0:
#         print(i)
# Count Multiples
# n=int(input("Enter "))
# sum=0
# for i in range(1,n+1):
#     if i%7==0:
#         sum=sum+1
# print(sum)
# Factorial of a Number
# n=int(input("enter "))
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
# print(sum)
# Average of N User Inputs
# n=int(input("Enter= "))
# l=[]
# sum=0
# for i in range(1,n+1):
#     b=int(input("Enter "))
#     l.append(b)
# print(l)
# for z in l:
#     sum=sum+z
# print(sum/n)
# Squares Table
# n=int(input("Enter "))
# sum=1
# for i in range(1,n+1):
#     sum=i*i
#     print(i,":",sum)
# Product of N Numbers
# n=int(input("Enter "))
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
# print(sum)
# Only Positive Sum
# n=(input("Enter 5 number = ").split(","))
# sum=0
# for i in n:
#     c=int(i)
#     if c > 0:
#         sum=sum+c
# print(sum)
# Power without ** Operator
# base=int(input("Enter "))
# exp=int(input("Enter "))
# sum=1
# for i in range(1,exp+1):
#     sum=(sum*base)
# print(sum)
# Leap Year Range
# for i in range(2000,2026,1):
#     if i % 4==0:
#         print(i)
# Find Maximum
# n=input("enter ").split(",")
# l=[]
# for i in n:
#     l.append(i)
# max=max(l)
# print(max)
# Find Minimum
# n=input("enter ").split(",")
# l=[]
# for i in n:
#     l.append(i)
# min=min(l)
# print(min)
# Number Category Counter
# n=input("enter ").split(",")
# sum=0
# for i in n:
#     z=int(i)
#     if z > 100:
#         sum=sum+1
# print(sum)

# Sum of Squares
# n=int(input("Enter "))
# sum=0
# mult=1
# for i in range(1,n+1):
#     mult=i*i
#     sum=mult+sum
# print(sum)
# Odd/Even Separator
# for i in range(1,11):
#     if i % 2==0:
#         print(i,":","Even")
#     else:
#         print(i,":","Odd")
# Divisibility Check in Range
# d=int(input("enter "))
# l=int(input("enter "))
# for i in range(1,l+1):
#     if i%d==0:
#         print(i)
# Count Down and Sum
# n=int(input("Enter "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     print(i)
# print("Total: ",sum)
# Multiplication Table (Custom)
# n=int(input("Enter "))
# multi=1
# for i in range(1,11):
#     multi=i*n
#     print(multi)

# Print a solid square grid of asterisks (`*`) with dimensions N x N.
# n=4
# for i in range(n):
#     # print(i)
#     for j in range(n):
#         print("*",end=" ")
#     print()
# Print a right-angled triangle pattern where row number dictates the count of asterisks.
# n=4
# for i in range(1,n+1):
#     # print(i)
#     for j in range(0,i):
#         print("*",end="")
#     print()

# Print a right-angled triangle upside down, decreasing the asterisk count per row.
# n=4
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*",end="")
#     print()

# Print a right-angled triangle mirrored horizontally, using leading spaces.
# n=4
# for i in range(n):
#     # print(i)
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*", end=" ")
#     print()

# Print a right-angled triangle where each item displays its current row index value.
# n=4
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# Print a right triangle using sequential numbers increasing systematically (Floyd's Triangle).
# n=4
# counter=0
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         counter=counter+1
#         print(counter,end=" ")
#     print()

# Print a right triangle of alternating 1s and 0s based on index positioning metrics.
# n=4
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
# Print an equidistant space-padded classic odd-numbered asterisk pyramid
# n=4
# for i in range(1,n+1):
#     # print(i)
#     for j in range(n-i,-1,-1):
#         print(" ",end="")
#     for z in range(1,i*2,1):
#         print("*",end="")
#     print()
# Print a classic odd-numbered asterisk pyramid upside down.
# n=4
# for i in range(1,n+1):
#     for j in range(0,i-1):
#         print(" ",end="")
#     for z in range(2*(n-i)+1):
#         print("*", end="")
#     print()
# Combine a standard and inverted pyramid sequence to structure a perfectly symmetric diamond.
# n=4
# for i in range(1,n+1):
#     for j in range(n-i,-1,-1):
#         print(" ", end="")
#     for z in range(1,i*2,1):
#         print("*",end="")
#     print()
# for d in range(2,n+1):
#     for h in range(-1,d-1,1):
#         print(" ",end="")
#     for c in range(2*(n-d)+1):
#         print("*",end="")
#     print()

# Print an N x N square outline using asterisks for borders and empty spaces internally.
# n=4
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Print a symmetric space-padded pyramid where each row reads as a numeric palindrome.
# n=4
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for z in range(1,i+1):
#         print(z,end="")
#     for m in range(z-1,0,-1):
#         print(m,end="")
#     print()

# Print a right-angled triangle changing letters chronologically by row positioning index.
# n=4
# b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(b[i],end="")
#     print()
# Print a sequential right triangle where character variables increment across lines consistently.
# n=4
# b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# c=0
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(b[c],end="")
#         c=c+1
#     print()
# Print a right-pointing arrow structure by running an increasing triangle into a decreasing one.
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for z in range (n-1,-1,-1):
#     for m in range(z-1,-1,-1):
#         print("*",end="")
#     print()
# # Merge an inverted pyramid structure directly into a standard odd pyramid layout.
# n=4
# for b in range(2*n-1,-1,-2):
#     for j in range(0,(2*n-b)//2):
#         print(" ",end="")
#     for z in range(b):
#         print("*",end="")
#     print()
# for i in range(2,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for z in range(1,i*2,1):
#         print("*",end="")
#     print()
# Print an N x N dimensional matrix representing an 'X' symbol framework using diagonal detection.
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Print a standard odd pyramid outline, preserving only the boundary asterisks.
# n=4
# for i in range(1,n+1):
#     for j in range(n-i,-1,-1):
#         print(" ",end="")
#     for z in range(1,i*2,1):
#         if z==1 or z==(2*i-1) or i==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Print an arithmetic triangle pattern calculating adjacent positional item coefficients.
# n = 4
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         if k == 0 or k == i:
#             print(1, end=" ")
#         else:
#             print(i, end=" ")
#     print()

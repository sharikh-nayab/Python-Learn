# Leap Year Algorithm: Write a script to check if a year provided by the user is a leap year.
# Ensure century years are only leap years if divisible by 400.
# leap=int(input("enter year= "))
# if leap % 4==0 :
#     print("Leap year")
# elif leap % 400 != 0:
#     print("Not a leap year")
# else:
#     print("Not a leap year")

# Binary Power Check: Use Bitwise Operators to determine if an integer is a power of 2. You
# are restricted from using any loops or external libraries.
# a=int(input("Enter value= "))
# b=a&(a-1)==0
# print(b)

#  Coordinate Geometry: Given x and y coordinates, find the quadrant. Handle cases where
# the point lies on the X-axis, Y-axis, or Origin.
# a=int(input("Please enter value "))
# b=int(input("Please enter value "))
# if a > 0 and b >0:
#     print("1")
# elif a < 0 and b > 0:
#     print("2")
# elif a < 0 and b < 0:
#     print("3")
# elif a > 0 and b < 0:
#     print("4")
# elif a != 0 and b == 0:
#     print("X")
# elif a==0 and b != 0:
#     print("Y")
# else:
#     print("Origin")

#  Logical Overlap: Given two intervals [a, b] and [c, d], write a single logical expression
# using comparison operators to detect if they overlap.
# a=[1,10]
# b=[11,15]
# if a[1] > b[0]:
#     print("Overlap")
# else:
#     print("No")

# Bitwise Odd-Even: Identify if a number is even or odd without using the modulo (%)
# operator. Use bitwise AND.
# a=int(input("Enter the number = "))
# if a&1:
#     print("Odd")
# else:
#     print("Even")

# Triangle Validity & Classification: Input three sides. Check if the triangle is valid. If valid,
# classify it as Equilateral, Isosceles, or Scalene.
# a=int(input("Enter value = "))
# b=int(input("Enter value = "))
# c=int(input("Enter value = "))
# if a + b > c and a + c > b and c + b > a:
#     print("Valid Triangle")
#     if a==b and a==c and c==b:
#         print("Equilateral Triangle")
#     elif a!=b and b!=c and a!=c:
#         print ("Scalene triangle")
#     else:
#         print("Isoceles Triangle")
# else:
#     print("Not a valid triangle")

# Zero-Safe Division: Perform a division a/b. If b is zero, display a custom error message.
# Otherwise, display the floor quotient and remainder.
# a=int(input("Enter Number = "))
# b=int(input("Enter Number = "))
# if b==0:
#     print("Error")
# elif b !=0:
#     c=a//b
#     d=a%b
#     print("Q", c,"R",  d)
# Max of Three: Find the maximum among three numbers using nested if-else statements
# (Strictly no max() function)
# a=int(input("Enter number = "))
# b=int(input("Enter number = "))
# c=int(input("Enter Number = "))
# print(a,b,c)
# if a > b >c:
#     print("a", a)
# elif b > c:
#     print("b",b)
# else:
#     print("c", c)    
    
# Bitwise Swap: Swap the values of two integer variables using the XOR (^) operator without
# using a temporary variable.
# a=7
# b=10
# a=a ^ b
# b=a ^ b
# a=a^b
# print("a=",a,"b=",b)

# Grading Logic: Calculate grade based on percentage: >90 (A), 80-90 (B), 70-80 (C), Below
# 70 (D). Use precise logical boundaries.
# a=int(input("Enter Value= "))
# if a >= 90:
#     print("A")
# elif a > 80 and a < 90:
#     print("B")
# elif a > 70 and a < 80:
#     print("C")
# elif a < 70:
#     print("D")

# Salary Breakdown: Calculate Net Salary. If Basic > 50k: HRA=20%, DA=90%. If Basic <=
# 50k: HRA=15%, DA=85%.
# a=int(input("Enter value= "))
# if a > 50000:
#     HRA = 0.2*a
#     DA= 0.9*a
#     Net=HRA+DA+a
#     print(Net)
# else:
#     HRA = 0.2*a
#     DA= 0.9*a
#     Net=HRA+DA+a
#     print(Net)

#  ASCII Character Analysis: Input a character and determine if it is Uppercase, Lowercase,
# Digit, or Special Symbol using ordinal comparisons.
# a=(input("Enter = "))
# b=ord(a)
# print(b)
# if b in range(65,90):
#     print("Uppercase")
# elif a in range(97,122):
#     print("Lowercase")
# elif a in range(48,57):
#     print("Digits")
# else:
#     print("Special characters")

# Dual Divisibility: Check if a number is divisible by 5 AND 11. If not, check if it's divisible
# by either one and print accordingly.
# a=int(input("Enter "))
# if a % 5 ==0 and a % 11==0:
#     print("Divisible by both")
# elif a % 5 ==0:
#     print("Divisible by 5")
# elif a % 11 ==0:
#     print("Divisible by 11")
# else:
#     print("Not divisible")
# 3-Digit Palindrome: Input a 3-digit number. Reverse it using arithmetic operators and
# check if the number is a palindrome
# a = int(input("Enter number = "))
# original = a
# reverse = 0
# while a != 0:
#     digit = a % 10
#     reverse = reverse * 10 + digit
#     a = a // 10
# print("Reversed number =", reverse)
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Progressive Electricity Billing: 1-50 units: 0.50/u; 51-150: 0.75/u; 151-250: 1.20/u; Above
# 250: 1.50/u. Add 20% surcharge to total.


    

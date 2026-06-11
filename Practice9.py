# Natural Sum Series: Write a function sum_natural(n) to calculate the sum of the series: 1 + 2
# + 3 + ... + n.
# def sumnatural(n):
#     a=n*(n+1)/2
#     return a
# print(sumnatural(5))

# Square Series: Write a function sum_squares(n) to calculate: 1² + 2² + 3² + ... + n².
# def sum_square(n):
#     sum=0
#     for i in range(1,n+1):
#         a=i*i
#         sum=sum+a
#     print(sum)
# sum_square(4)

# Alternating Sign Series: Create a function to solve: 1 - 2 + 3 - 4 + 5 ... up to n terms
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum=sum-i
#         if i%2!=0:
#             sum=i+sum
#     print(sum)
# sum(5)

# Power Series: Write a function power_sum(x, n) to compute: 1 + x + x² + x³ + ... + xⁿ.
# def power(x,n):
#     s=0
#     for i in range(0,n+1):
#         s=s+pow(x,i)
#     print(s)
# power(2,3)
# Factorial Division Series: Solve the series: 1/1! + 2/2! + 3/3! + ... + n/n!.
# def series(n):
#     s=1
#     b=0
#     for i in range(1,n+1):
#         s=(s*i)
#         b=b+(i/s)
#     print(b)
# series(3)

# Geometric Progression: Write a function to find the sum of a GP: a + ar + ar² + ... up to n terms.
# def gp(a,r,n):
#     s=0
#     for i in range(n):
#         b=a*pow(r,i)
#         s=s+b
#     print(s)
# gp(2,3,3)

# Special Number Series: Calculate the sum: 1 + 11 + 111 + 1111 + ... up to n terms.
# def sum(n):
#     s=0
#     t=0
#     for i in range(1,n+1):
#         s=s*10+1
#         t=t+s
#     print(t)
# sum(5)

# Harmonic Progression: Compute the sum of 1 + 1/3 + 1/5 + 1/7 + ... up to n terms.
# def sum(n):
#     s=0
#     for i in range(1,n+3,2):
#         a=1/i
#         s=s+a
#     print(s)
# sum(3)

# Fibonacci Sum: Create a function that calculates the sum of the first n Fibonacci numbers.
# def fib(n):
#     a=0
#     b=1
#     s=0
#     for i in range(n):
#         next=a+b
#         next=a
#         a=b
#         s=s+a
#     print(s)
# fib(4)

# Factorial Fraction: Solve the series: x/1! - x³/3! + x⁵/5! - x⁷/7! ... up to n terms.
# Input
# x = int(input("Enter x: "))
# n = int(input("Enter number of terms: "))
# total = 0
# odd = 1  # 1, 3, 5, 7...
# for term in range(1, n + 1):
#     # Calculate x^odd
#     power = x ** odd
#     # Calculate odd!
#     factorial = 1
#     for i in range(1, odd + 1):
#         factorial *= i
#     # Create fractio
#     fraction = power / factorial
#     # Apply sign
#     if term % 2 == 1:      # 1st, 3rd, 5th term
#         total += fraction
#     else:                  # 2nd, 4th, 6th term
#         total -= fraction
#     odd += 2
# print("Answer =", total)
# Even-Odd Power: Solve the series: 1¹ + 2² + 3³ + 4⁴ + ... + nⁿ
# def se(n):
#     s=0
#     for i in range(1,n+1):
#         a=pow(i,i)
#         s=s+a
#     print(s)
# se(3)
# Prime Series Sum: Write a function to find the sum of the first n prime numbers.
# n = 3
# count = 0
# num = 2
# total = 0
# while count < n:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         total += num
#         count += 1
#     num += 1
# print(total)

# Custom Digit Series: Solve: x + xx + xxx + ... up to n terms (where x is a digit between 1-9).
# def c(n):
#     t=0
#     s=0
#     for i in range(1,n+1):
#         s=s*10+5
#         t=s+t
#     print(t)
# c(3)

# Triangular Number Series: Find the sum of the first n triangular numbers (1, 3, 6, 10, 15...)
# def tri(n):
#     s=0
#     for i in range(1,n+1):
#         a=i*(i+1)/2
#         s=s+a
#     print(s)
# tri(3)

# Nested Factorial Sum: Calculate: 1! + (1!+2!) + (1!+2!+3!) + ... up to n blocks.
# def fact(n):
#     s=1
#     a=0
#     b=0
#     for i in range(1,n+1):
#         s=s*i
#         a=a+s
#         b=a+b
#     print(b)
# fact(5)
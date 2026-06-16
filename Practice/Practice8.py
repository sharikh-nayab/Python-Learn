# Write a program to calculate the total length of a user-provided string. 
# s=input("Enter ")
# print(len(s))
# Create a program to count how many times the character 'e' appears in the word
# "Excellence" (case-insensitive). 
# s="Excellence"
# print(s.count("e"))
# Accept a full name from the user and display it entirely in uppercase. 
# s=input("enter ")
# print(s.upper())
# Write a program to check if a string starts with the prefix "Python". 
# s="Python programming"
# print(s.startswith("Python"))
# s=input("enter ")
# st=len(s)
# m=st//2
# print(s[m])
# Extract the first three characters of a string using slicing. 
# s=input("Enter ")
# for i in s[0:3:1]:
#     print(i)
# Extract the last four characters of a string using negative indexing.
# s=input("enter ")
# for i in s[-1:-5:-1]:
#     print(i)
# Write a program to reverse a given string without using a loop
# s=input("enter ")
# t=s[::-1]
# print(t)
# 279. Check if a string is a palindrome (reads the same forward and backward). 
# a=input("enter ")
# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# 280. Write a program to count the total number of vowels (a, e, i, o, u) in a string. 
# a=input("Enter ")
# b=["a","e","i","o","u"]
# sum=0
# for i in a:
#     # print(i)
#     if i in b :
#         sum=sum+1
# print("total number of vowel",sum)
# 281. Replace all occurrences of the word "bad" with "good" in a sentence.
# n="This is a bad day with some bad weather."
# if "bad" in n:
#     b=n.replace("bad","good")
#     print(b)
#  Accept a sentence and count the total number of words it contains. 
# n=input("enter ")
# sum=0
# for i in n:
#     sum=sum+1
# print(sum)
# Display every alternate character of a string starting from the first character
# n=input("enter ")
# for i in n[0::2]:
#     print(i)
#  Write a program to check if a string contains only numeric digits. 
# n=input("enter ")
# a=n.isdigit()
# print(a)
# Remove all leading and trailing whitespace from a user-inputted string
# a="    sharikh    "
# b=a.strip()
# print(b)
# Capitalize only the first letter of a given sentence. 
# a="sharikh"
# b=a.capitalize()
# print(b)
# Write a program to check if a specific substring exists within a string using the in
# operator. 
# a=input("enter ")
# b=input("check substring ")
# if b in a:
#     print(True)
# else:
#     print(False)
# . Given two strings, concatenate them with a space in between. 
# a="hello"
# b="world"
# c=a+" "+b
# print(c)
# Repeat a string "Alert!" five times using the replication operator
# a="Alert"
# b=a*5
# print(b)
# Find the index of the first occurrence of the letter 'z' in a string. 
# n="ezbroz"
# print(n.index("z"))
# Write a program to convert a string to a list of its individual characters.
# a="python"
# b=[]
# for i in a:
#     b.append(i)
# print(b)
# Convert a list of strings ['Python', 'is', 'fun'] into a single space-separated sentence. 
# a="Python is fun"
# print(a.split())
# Swap the case of a string (uppercase becomes lowercase and vice versa). 
# a="Python is fun"
# print(a.swapcase())
# Write a program to check if a string ends with the suffix ".pdf". 
# a="Python.pdf"
# print(a.endswith(".pdf"))
# . Count the total number of uppercase letters in a string. 
# a="Python ProGrammIng"
# sum=0
# for i in a:
#     if i.isupper():
#         sum=sum+1
# print(sum)
# Extract a substring from index 2 to index 8 with a step of 2
# a="PythonProgramming"
# for i in a[2:8:2]:
#     print(i)
# Write a program to remove the character at a specific index from a string
# a="Python"
# b=[]
# # print(b)
# for i in a:
#     b.append(i)
# b.pop(1)
# print(b)
# Count how many times the word "the" appears in a long paragraph.
# a="the cat sat on the mat. The dog watched the cat while the bird flew away"
# b=a.count("the")
# print(b)
# Write a program to find the highest alphabetical character in a string using the max() function. 
# a="Python"
# b=max(a)
# print(b)
# Write a program to find the lowest alphabetical character in a string using the min() function. 
# a="Python"
# print(min(a))
# Check if a string contains any special characters (like @, #, $, %). 
# a="Python@"
# if a.isalpha() or a.isdigit():
#     print("Not a special character")
# else:
#     print("Special Character")
# Split a comma-separated string of items (e.g., "bread,milk,eggs") into a list
# a="bread,milk,eggs"
# a=a.split(",")
# b=list(a)
# print(b)
# Write a program to pad a string with zeros until it reaches a length of 10 characters. 
# a="python"
# print(a.zfill(10))
# Display a string in a "vertical" format (one character per line) using a loop. 
# a="Python"
# for i in a:
#     print(i)
# Concatenate a string and an integer by converting the integer to a string first. 
# s="Age"
# i= 25
# i=str(i)
# b=i+s
# print(b)
# Write a program to count the number of spaces in a sentence. 
# a="Python is easy to learn"
# print(a.count(" "))
# Check if a given string is a valid title 
# a="python Programming Language"
# if a.istitle():
#     print("valid")
# else:
#     print("Not valid")
# Reverse only the words in a sentence, but keep the words in their original order. 
# a="Python is fun"
# b=a.split()
# result=""
# for i in b:
#     result=result+i[::-1]+" "
# print(result)
# Extract the domain name from an email address string (e.g., "neha@bcsbca.com" ->
# "bcsbca.com"). 
# a="neha@bcsbca.com"
# b=a.split("@")
# print(b[1])
# Write a program to multiply the string "Python" by the number of times the letter 'a'
# appears in "Banana".
# a="python"
# b="banana"
# sum=0
# for i in b:
#     if "a" in i:
#         sum=sum+1
# print(sum*a)
# A GPS system stores location as (latitude, longitude). Write a function that takes a list of coordinate tuples
# and returns only those that are within the 'Northern Hemisphere' (Latitude > 0).
# a=[(18.5, 73.8), (-33.8, 151.2)]
# a=[(0, 78.9)]
# a=[]
# b=[]
# for i in a :
#     # print(i[0])
#     if i[0] > 0:
#         # b.append(i)
#         print(i)
# print(b)
# An HR database stores employee data as (ID, Name, Dept). Given a tuple of these records, find the index
# of the employee with ID 105. If not found, return -1.
# a=((101, 'Ram', 'IT'), (105, 'Neha', 'HR'))
# a=((101, 'Ram', 'IT'),) 
# for i in a:
#     if i[0] ==105:
#         b=a.index(i)
#         print(b)
#     else:
#         print(-1)
# Stock prices for a week are stored in a tuple. Calculate the price difference between the first and the last
# day of the week using indexing.
# a=(150, 155, 148, 160)
# a=(200, 190, 180)
# a=(100,)
# for i in a[-1::-1]:
#     b=a[len(a)-1]-a[0]
# print(b)
# System configurations are stored in a tuple to prevent accidental changes. Write a script to count how
# many times the value 'Enabled' appears in the config tuple.
# a=('Enabled', 'Disabled', 'Enabled') 
# a=('Disabled', 'Pending')
# if "Enabled" in a:
#     b=a.count("Enabled")
#     print(b)
# else:
#     print("0")
# A database query returns a row as (User_ID, Username, Email, City). Unpack this tuple into variables and
# return a formatted string: 'User [Username] lives in [City]'.
# a=(1, 'prof_ram', 'ram@logic.com', 'Pune')
# for i in a:
#     User_id=a[0]
#     Username=a[1]
#     Email=a[2]
#     City=a[3]
# print(f"User {Username} lives in {City}")
# A tuple contains logs for the last 10 years. Use slicing to extract the records for the 'mid-range' years
# (index 4 to 7 inclusive).
# a=(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,2019)
# a=a[4:8:1]
# print(a)
# A shipping company accepts packages if the sum of dimensions (Length, Width, Height) is less than 100.
# Given a tuple of 3 integers, return 'Accept' or 'Reject'.
# a=(30, 30, 30)
# a=(50, 25, 25) 
# am=0
# for i in a:
#     # print(i)
#     am=am+i
# # print(am)
# if am < 100:
#     print("accepted")
# else:
#     print("rejected (Sum is 100)")
# To form a secure key, you need to merge two tuples of characters. Create a new tuple by joining Tuple A
# and Tuple B.
# a=('A', 'B')
# b=('C', 'D')
# c=a+b
# print(c)
# You are given an input. Your task is to ensure it is returned as a tuple. If it's a single integer `n`, return
# `(n,)`.
# a=5
# a=(1,2)
# b=tuple()
# if type(a)==int:
#     b=b+(a,)
#     print(b)
# else:
#     print(a)
# Given a list of tuples representing (Student_Name, Marks), sort the list based on Marks in descending
# order.
# a = [('A', 80), ('B', 95), ('C', 85)]
# for i in range(len(a)):
#     print(i)
#     for j in range(i + 1, len(a)):
#         print(j)
#         if a[i][1] < a[j][1]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)

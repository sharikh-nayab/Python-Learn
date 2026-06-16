# 1. Email Domain Filter
# A company wants to separate internal emails from external ones. Given a list of email strings, return a new list
# containing only those that belong to the 'logic-overflow.com' domain
# a=['ram@gmail.com', 'neha@logicoverflow.com', 'hr@logicoverflow.com']
# b=['test@yahoo.com'] 
# c=[]
# d=[]
# for i in a:
#     if "@logicoverflow.com" in i:
#         d.append(i)
# print(d)
# if "@logicoverflow.com" not in b:
#     print([])
# if "@logicoverflow.com" not in c:
#     print([])
# Due to a global tax change, increase every item's price in a list by exactly 5%. Round the result to 2 decimal places.
# a=[100, 200, 300] 
# n=[]
# b=[0, 50] 
# m=[]
# c=[10.5]
# d=[]
# for i in a:
#     z=0.05*i
#     i=i+z
#     n.append(i)
# print(n)
# for i in b:
#     z=0.05*i
#     i=i+z
#     m.append(i)
# print(m)
# for i in c:
#     z=0.05*i
#     i=i+z
#     j=round(i,2)
#     d.append(j)
# print(d)
# Simulate a simple FIFO (First In First Out) queue. Given an initial queue and a list of new tasks, add the new tasks and
# then remove the first two tasks from the front.
# a=['T2', 'T3','T4']
# b=['T1']
# a.insert(0,b[0])
# # print(a)
# for i in a[0:2]:
#     a.remove(i)
# print(a)
# d=['T1']
# n=[]
# d.pop(2)
# A database export has duplicates. Extract unique IDs from the list while preserving the original order of their first
# appearance.
# a=[10, 20, 10, 30, 20]
# u=[]
# for i in a:
#     if i not in u:
#         u.append(i)
# print(u)
# a=[1, 2, 3] 
# u=[]
# for i in a:
#     if i not in u:
#         u.append(i)
# print(u)
# a=['A', 'A', 'A'] 
# u=[]
# for i in a:
#     if i not in u:
#         u.append(i)
# print(u)
# A warehouse stacker needs to process packages in the reverse order of how they were received. Reverse the list inplace without using `[::-1]`.
# a=[1, 2, 3, 4]
# u=[]
# for i in a[len(a)-1::-1]:
#     u.append(i)
# print(u)
# a=['A', 'B', 'C'] 
# u=[]
# for i in a[-1::-1]:
#     u.append(i)
# print(u)
# Given a list of employee performance scores, find the top 3 highest scores. If there are fewer than 3 scores, return all
# of them sorted descending.
# a=[88, 92, 78, 99, 100]
# a.sort(reverse=True)
# print(a[0:3])
# a=[95, 80] 
# a.sort(reverse=True)
# print(a[0:])
# a=[100, 100, 90]
# a.sort(reverse=True)
# print(a[0:])
# Check if 'Router' exists in a list of network hardware. If found, return its index. If not, add it to the end of the list and
# return the new list
# a=['Switch', 'Router', 'Hub']
# if "Router" in a:
#     print(f"found: {a.index("Router")}")
# a=['Switch', 'Hub'] 
# if "Router" not in a:
#     a.append("Router")
#     print(a)
# From a list of 100 log entries, extract the first 5 (Recent) and last 5 (Oldest) using list slicing in a single program.
# u=[]
# for i in list(range(1,101)):
#     u.append(i)
# print("First:",u[0:5])
# print("Last:",u[-1:-6:-1])
# n=[1,2,3]
# print("first:",n[0:],"last:",n[0:])
# a=[10,5]
# b=[8,12]
# a.extend(b)
# a.sort(reverse=False)
# print(a)
# a=[]
# b=[1,2]
# a.extend(b)
# a.sort(reverse=False)
# print(a)
# In a sorted list of IDs, find the middle element. For even-length lists, return a list containing the two middle elements.
# a=[10,20,30]
# b=[1,2,3,4]
# # for i in a[1:2]:
# #     print(i)
# for i in b[1:3]:
#     print(i)
# Count how many times the word 'Python' appears in a list of tags. Ensure the search is case-insensitive.
# a=['python', 'PYTHON', 'java']
# a=['C++', 'JS']
# c="python"
# sm=0
# for i in a:
#     b=i.lower()
#     if c==b:
#         v=b.count(b)
#         sm=sm+v
# print(sm)
# Remove the single highest and single lowest score from a list of judges' marks to find the filtered list.
# a=[9.5, 8.0, 10.0, 7.5] 
# a.remove(10.0)
# a.remove(7.5)
# a=[5, 5, 10, 8] 
# a.remove(5)
# a.remove(10)
# print(a)
# Check if a list of characters forms a palindrome (reads the same forward and backward).
# a=['n', 'i', 't', 'i','n']
# a=['a', 'b', 'c'] 
# b=[]
# for i in a[::-1]:
#     b.append(i)
# if a==b:
#     print(True)
# else:
#     print(False)
# Given a list of 20 customer IDs, split them into exactly 4 batches of 5 IDs each using slicing.
# n=[]
# a=[]
# b=[]
# c=[]
# d=[]
# for i in list(range(1,21)):
#     n.append(i)
# for v in n[0:5]:
#     a.append(v)
# for z in n[5:10]:
#     b.append(z)
# for t in n[11:15]:
#     c.append(t)
# for y in n[16:20]:
#     d.append(y)
# print(a,b,c,d)
# Sort a list of guest names alphabetically, but ensure any name starting with 'Z' is moved to the very front.
# a=['Alice', 'Zayn', 'Bob', 'Zara']
# a=['Adam', 'Bill'] 
# b=[]
# c=[]
# for i in a:
#     # print(i)
#     if "Z" in i:
#         b.append(i)
#     else:
#         c.append(i)
# b.extend(c)
# print(b)
# From a list of transactions, extract all negative values (expenses) into a new list named 'Alerts'.
# a=[500, -20, 100, -5]
# a=[10, 20] 
# b=[]
# for i in a:
#     # print(i)
#     if i < 0:
#         b.append(i)
# print(b)
# In a theater seating list where 'None' represents an empty seat, find the index of the first 'None'. Return -1 if full.
# a=['Occupied', 'Occupied'] 
# if None in a:
#     b=a.index(None)
#     print(b)
# else:
#     print("-1")
# Given a list of words from a news headline, swap the first and the last word using indexing.
# a=['Python', 'is', 'Great']
# a=["Hello"]
# b=[]
# for i in a[::-1]:
#     b.append(i)
# print(b)
# A list contains 'Free' and 'Paid'. Use a loop to find every 'Free' instance and replace it with 'Trial'.
# a=['Free', 'Paid', 'Free'] 
# a=['Paid'] 
# for i,b in enumerate(a):
#     # print(i,b)
#     if "Free"== b:
#         a[i]="Trail"
# print(a)
# Convert a matrix (list of lists) like [[1,2], [3,4]] into a single dimension list [1,2,3,4].
# a=[[1, 2], [3, 4]]
# a=[[1], [2, 3], []]
# b=[]
# c=[]
# d=a[0]
# n=a[1]
# d.extend(n)
# print(d)
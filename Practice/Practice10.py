# Two Sum
# n=[2,7,11,15]
# for i in range(len(n)):
#     for j in range(i):
#         if n[i]+n[j]==9:
#             print(i,j)

# Valid Anagram 
# s = "anagram"
# t = "nagaram"
# b={}
# c={}
# for i in s:
#     b.update({i:s.count(i)})
# for j in t:
#     c.update({j:t.count(j)})
# if b==c:
#     print(True)
# else:
#     print(False)

# Contains Duplicate
# n=[1,2,3,1]
# b=set(n)
# if len(b) != len(n):
#     print(True)
# else:
#     print(False)

# Group Anagrams
# s=["eat","tea","tan","ate","nat","bat"]
# b={}
# for i in s:
#     a="".join(sorted(i))
#     if a in b:
#         b[a].append(i)
#     else:
#         b.update({a:[i]})
# print(b)

# Longest Substring Without Repeating Characters
# s="abca"
# a={}
# start=0
# total_lenght=0
# for index,char in enumerate(s):
#     if char in a:
#         start=a[char]+1
#         a.update({char:index})
#         current_length=index-start+1
#         if current_length>total_lenght:
#             total_lenght=current_length
#     else:
#         a.update({char:index})
# print(total_lenght)

# Top K Frequent Elements
# nums = [1,1,1,2,2,3]
# a={}
# c=[]
# for i in nums:
#     a.update({i:nums.count(i)})
# b=a.items()
# s=sorted(b, key=lambda x:x[1], reverse=True)
# for j in s[0:2]:
#     c.append(j[0])
# print(c)

# Merge Intervals
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# a=[]
# ci=intervals[0]
# for i in intervals[1:]:
#     if i[0]<=ci[1]:
#         ci=[ci[0],max(ci[1],i[1])]
#     else:
#         a.append(ci)
#         ci=i
# a.append(ci)
# print(a)

# Longest Consecutive Sequence 
# s=[100,4,200,1,3,2]
# a=set(s)
# longest_length =0
# for i in a:
#     if i - 1 not in a:
#         current_num=i
#         current_length=1
#         while current_num+1 in a:
#             current_num=current_num+1
#             current_length=current_length+1
#         longest_length=max(longest_length,current_length)
# print(longest_length)

# Subarray Sum Equals K
# nums = [1, 1, 1]
# k = 2
# c=0
# for i in range(len(nums)):
#     cs=0
#     for j in range(i, len(nums)):
#         cs=cs+nums[j]
#         if cs == k:
#             c=c+1
# print(c)


# s = "ADOBECODEBANC"
# t = "ABC"
# smallest = ""
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         substring = s[i:j + 1]
#         valid = True
#         for char in t:
#             if substring.count(char) < t.count(char):
#                 valid = False
#                 break
#         if valid:
#             if smallest == "":
#                 smallest = substring
#             elif len(substring) < len(smallest):
#                 smallest = substring
# print(smallest)

    

# nums = [2,7,11,15]
# target = 9
# nums = [3,2,4]
# target = 6
# for i in range(len(nums)):
#     # print(i)
#     current=nums[i]
#     needed=target - nums[i]
#     if needed in nums:
#         a=nums.index(needed)
#         if a !=i:        
#             out.append(i)
#             out.append(a)
#             break
# print(out)
# nums = [3,3]
# target = 6
# out=[]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i !=j:
#             if nums[i] + nums[j] == target:
#                 out.append(i)
#                 out.append(j)
#                 break
#     if len(out) > 0:
#         break
# print(out)
# nums = [1,2,2,1]
# k = 1
# nums = [1,3]
# k = 3
# nums = [3,2,1,5,4]
# k = 2
# sum=0
# for i in range(len(nums)):
#     # print(nums[i])
#     for j in range(len(nums)):
#         if i < j:
#             if abs(nums[i] - nums[j])==k:
#                 sum=sum+1
# print(sum)

        
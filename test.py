# nums = [1,2,3,4,5]
# res = []
# count = 0
# while sum(nums) > sum(res):  
#     res.append(nums[count])
#     count += 1
#     nums = nums[1:]
#     print(nums.pop(1))
# print(nums)
# res,curr = [],0
#         if len(nums) <=1:
#             return sum(nums)
#         for i in range(len(nums)-1):
#             res.append(nums[i])
#             if len(res) == k:
#                 if curr < sum(res)/k:
#                     curr = sum(res)/k
#                 res.pop(0)
            
#         return curr

s = 'The Sky is Blue'
s= s.split(" ")
s = ' '.join(reversed(s))
print(s)
# Path: test.py
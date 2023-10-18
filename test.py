nums = [1,2,3,4,5]
res = []
count = 0
while sum(nums) > sum(res):  
    res.append(nums[count])
    count += 1
    nums = nums[1:]
    print(nums.pop(1))
print(nums)

# Path: test.py
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#target = 9
target = 6
#target = 6
#nums = [2,7,11,15]
nums = [3,2,4]
#nums = [3,3]

def solution1(nums,target):
    found = False
    for j in range(0,len(nums)-1):
        for i in range(j+1,len(nums)):
            if(nums[i]+nums[j] == target):
                found = True
                break
        if found: 
            break
    return [j,i] if found else []

def solution2(nums,target):
    dic = {nums[i]:i for i in range(0,len(nums))} # dict

    for index,number in enumerate(nums):
        complement = target - number
        if ((complement in dic) and (dic[complement] != index)):
            return [index,dic[complement]] if index<complement else [dic[complement],index]
    return []

def solution3(nums,target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]],i]
        else:
            required[nums[i]]=i

print(solution1(nums,target))
print(solution2(nums,target))
print(solution3(nums,target))
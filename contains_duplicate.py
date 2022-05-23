'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def containsDuplicate(nums):
    return len(nums) == len(set(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1,2,3,4]
res = containsDuplicate(nums)
print(res)

        
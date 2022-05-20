'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space
'''

def singleNumber(nums):
    # math formula
    # 2*(a+b+c) - (2a+2b+c) = c
    # summation of unique elements - summation of all elements gives you unique single number
    single_num = 2 * sum(set(nums)) - sum(nums)
    return single_num


nums = [4,1,2,1,2]
res = singleNumber(nums)
print(res)
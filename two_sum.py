# PROBLEM           (difficulty: easy)
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

'''


# SOLUTION
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # making a list of indexes
        num_lst = list(range(len(nums)))
        
        # enumerating through num_lst
        for index, num in enumerate(num_lst):
            # traversing num_lst with starting index being +1 of the upper for loop
            for num_other in num_lst[index+1:]:
                # checking for the target by comparing every addition
                if nums[num] + nums[num_other] == target:
                    # returning found indexes
                    return [num, num_other]
                else:
                    continue
                    
        return None
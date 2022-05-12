'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for x in range(j, len(nums)):
            nums[x] = 0
            
        return nums

nums = [0,1,0,3,12]

res = moveZeroes(nums)
print(res)
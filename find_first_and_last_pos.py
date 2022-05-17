'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity
'''

def getLeftPos(nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                if nums[mid-1] != target or mid == 0:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
def getRightPos(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left+right)//2
        
        if nums[mid] == target:
            if mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1:
                return mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1
    
def searchRange(nums, target):
    left = getLeftPos(nums, target)
    right = getRightPos(nums, target)
    
    return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8
res = searchRange(nums, target)
print(res)
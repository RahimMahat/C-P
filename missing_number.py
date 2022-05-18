'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

def missingNumber(nums) -> int:
        n = len(nums)
        currentSum = sum(nums)
        # using guass formula
        intendedSum = n*(n+1)/2
        
        missing_num = intendedSum - currentSum
        
        return int(missing_num)

nums = [3,0,1]
res = missingNumber(nums)
print(res)
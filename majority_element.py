'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

def majorityElement(nums):
    # using a hashmap to keep the count of numbers
    map = {}
    for num in nums:
        map[num] = map.get(num, 0) + 1

    for num in nums:
        if map[num] > len(nums)//2:
            return num

nums = [2,2,1,1,1,2,2]
res = majorityElement(nums)
print(res)
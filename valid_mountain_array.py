'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

def validMountainArray(arr) -> bool:
    if len(arr) < 3:
        return False
        
    i = 1
    # check for increasing subarray
    while i < len(arr) and arr[i] > arr[i-1]:
        i += 1
    if i == 1 or i == len(arr):             # if the pointer didn't move or it came to end then it's not valid mountain array
        return False
    # check for decreasing subarray
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1
        
    return i == len(arr)                    # after checking for increase and decrease subarrays if pointer came to an end then it is valid mountain array

arr = [0, 3, 2, 1]
res = validMountainArray(arr)
print(res)
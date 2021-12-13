##GFG

'''
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
'''

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far = arr[0]
        max_ending_here = 0
        for i in range(len(arr)):
            max_ending_here += arr[i]
            
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

sol = Solution()
arr= [1,2,3,-2,5]
n = len(arr)
print(sol.maxSubArraySum(arr, n))

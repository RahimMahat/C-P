##GFG
'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.

'''

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr = sorted(arr)
        avg = sum(arr)/n
        Arr = set()
        for i in arr:
            if i <= avg:
                i = i + k
            else:
                i = i - k
                
            Arr.add(i)
        ans = max(Arr) - min(Arr)
        return ans

k = 2
n = 4
arr = [1, 5, 8, 10]
sol = Solution()
print(sol.getMinDiff(arr, n, k))
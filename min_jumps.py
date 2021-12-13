## GFG
'''
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
Note: Return -1 if you can't reach the end of the array.
Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to last. 
'''



class Solution:

    def minJumps(self, arr, n):
	    # the number of jumps needs to reach the starteing index is 0
        if n <= 1:
            return 0
        
        # return -1 if not possible to jump
        if arr[0] == 0:
            return -1
            
        # store all time the maximal reachable index in the array
        maxReach = arr[0]
        # store the amount of steps we can still take
        step = arr[0]
        # stores the amount of jumps necessary to reach that maximal reachable position
        jump = 1
        
            
        for i in range(1, n):
            # check if we have reached the end of the array
            if i == n-1:
                return jump
            # updating maxReach
            maxReach = max(maxReach, i + arr[i])
            # we use a step to get to the current index
            step -= 1
            
            # if no further steps left
            if step == 0:
                jump += 1
                
                # check if the current index / postion or lesser index
                # is the maximum reach point from the previous indexes
                if i >= maxReach:
                    return -1
                    
                # re-initialize the steps to the amount
                # of steps to reach maxReach from position i
                step = maxReach - i

        return -1
    
sol = Solution()
n = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(sol.minJumps(arr, n))
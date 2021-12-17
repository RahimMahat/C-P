##LEETCODE

'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
'''

class Solution:
    def findMinArrowsShots(self, points):
        # sort the array with the end key
        points = sorted(points, key= lambda x: x[1])

        res, end = 0, -float('inf')
        # traverse through the array
        for interval in points:
            # check if the first element of arrays is greater than end element:
            if interval[0] > end:
                # if yes increase the counter of res
                res += 1
                # and set the end var to the end element of the current interval
                end = interval[1]

        return res

sol = Solution()
points = [[1,2],[3,4],[5,6],[7,8]]
print(sol.findMinArrowsShots(points))
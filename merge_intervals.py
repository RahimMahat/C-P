## LEETCODE

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

class Solution:
    def merge(self, intervals):
        # sort the array with starting element of each interval
        intervals.sort(key= lambda x: x[0])

        merged = []
        for interval in intervals:
            # check if the merged list is empty or
            # the starting element of interval is greater than ending element of already merged interval
            if not merged or interval[0] > merged[-1][1]:
                # then append the interval as is
                merged.append(interval)
            else:
                # otherwise update the end element of merged interval to the 
                # maximum of interval now end element or already merged end element
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
print(sol.merge(intervals))
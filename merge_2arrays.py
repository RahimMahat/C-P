## GFG
'''
Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.
Input:
N = 4, M = 5
arr1[] = {1, 3, 5, 7}
arr2[] = {0, 2, 6, 8, 9}
Output: 0 1 2 3 5 6 7 8 9
Explanation: Since you can't use any 
extra space, modify the given arrays
to form 
arr1[] = {0, 1, 2, 3}
arr2[] = {5, 6, 7, 8, 9}
'''


class Solution:

    def nextGap(self, gap):
        if gap <= 1:
           return 0
        return (gap // 2) + (gap % 2)
    
    def merge(self, arr1, arr2, n, m):
    
        gap = n + m
        gap = self.nextGap(gap)
        while gap > 0:
    
            # comparing elements in
            # the first array.
            i = 0
            while i + gap < n:
                if (arr1[i] > arr1[i + gap]):
                    arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
    
                i += 1
    
            # comparing elements in both arrays.
            j = gap - n if gap > n else 0
            while i < n and j < m:
                if (arr1[i] > arr2[j]):
                    arr1[i], arr2[j] = arr2[j], arr1[i]
    
                i += 1
                j += 1
    
            if (j < m):
    
                # comparing elements in the
                # second array.
                j = 0
                while j + gap < m:
                    if (arr2[j] > arr2[j + gap]):
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
    
                    j += 1
    
            gap = self.nextGap(gap)
            

        
if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n, m = map(int, (input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=' ')
        for x in arr2:
            print(x, end=' ')
        print()
        tc -= 1
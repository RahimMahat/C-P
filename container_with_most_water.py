'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container
'''

def maxArea(height) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        
        while left < right:
            # finding area of the rectangle
            maxarea = max(
                maxarea, min(height[left], height[right]) * (right-left)
            )
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea

height = [1,8,6,2,5,4,8,3,7]
res = maxArea(height)
print(res)
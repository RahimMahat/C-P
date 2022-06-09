## LEETCODE

# PROBLEM           (difficulty: easy)
'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''


# SOLUTION
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # two liner
        # y = str(x)
        # return y == y[::-1]
        
        if x < 0:
            return False
        
        number = x
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
            
        return x == reverse

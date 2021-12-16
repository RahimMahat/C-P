##LEETCODE
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()[]{}"
Output: true
Example 2:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # if length of string is odd then return false
        if len(s) % 2 != 0:
            return False
        # make dictionary of pairs
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
            }
        # using stack data structure for its LIFO property
        stack = []

        for char in s:
            # traverse through string and if char in keys of dictionary then push to stack
            if char in pairs.keys():
                stack.append(char)
            # if stack is empty or char doesn't match with the last element of the stack return false
            elif stack == [] or char != pairs[stack.pop()]:
                return False
        # after going through the stack and poping the element stack needs to be empty
        # if it's empty it'll return true else false
        return stack == []

sol = Solution()
s = r"()[]{}"
print(sol.isValid(s))
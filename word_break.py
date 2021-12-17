##LEETCODE
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code"
'''

class Solution:
    def wordBreak(self, s, wordDict):
        l = len(s)
        # create a list to mark start and end position of the word
        dp = [False] * (l+1)
        # mark first char to be true
        dp[0] = True

        # go through the string char by char
        for i in range(1, l+1):
            # using the previous char form a word
            for j in range(i):
                # check if they are in dictionary
                if dp[j] and s[j:i] in wordDict:
                    # mark the next char as true so that we know char before this form a word
                    # and where to start in next iteration
                    dp[i] = True
        
        return dp[-1]



sol = Solution()
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s, wordDict))
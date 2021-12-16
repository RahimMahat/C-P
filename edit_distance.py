##LEETCODE
'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''

class Solution:
    def minDistance(self, str1, str2):
        m = len(str1)
        n = len(str2)
        # create a table to store the result of subproblems
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # fill dp[][] in bottom-up manner
        for i in range(m + 1):
            for j in range(n + 1):
                # if first string is empty
                # insert all char in first string
                if i == 0:
                    dp[i][j] = j
                # if second string is empty
                # remove all char from first string
                elif j == 0:
                    dp[i][j] = i
                # if last char of both string are same
                # ignore last char and recur for remaining chars
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # if last char are not same then consider
                # all possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],      # insert
                                        dp[i-1][j],     # remove
                                        dp[i-1][j-1]    # replace
                                        )
        return dp[m][n]

        # time and space complexity: bigO(m*n)

sol = Solution()
str1 = "voldemort"
str2 = "dumbledore"
print(sol.minDistance(str1, str2))


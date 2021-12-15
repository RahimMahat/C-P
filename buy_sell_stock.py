## LEETCODE
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
    def maxProfit(self, prices) -> int:
        # define min and max value
        minprice = 999999999999
        maxprofit = 0
        # traversing through the array
        for i in range(len(prices)):
            if prices[i] < minprice:
                # finding the minimun price
                minprice = prices[i]
                # if the price at point and minimum price is greater than maxprofit
            elif prices[i] - minprice > maxprofit:
                # assign maxprofit to it
                maxprofit = prices[i] - minprice
        
        return maxprofit

sol = Solution()
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))
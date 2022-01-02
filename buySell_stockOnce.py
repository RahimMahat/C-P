'''
Write a program that takes an array denoting the daily stock price, and retums the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.
'''

def buy_and_sell_stock_once(prices):
    # keep track of min price and max profit
    min_price_so_far, max_profit = float('inf'), 0.0

    for price in prices:
        # calculate the max profit for current position
        max_profit_sell_today = price - min_price_so_far
        # assign max profit to the maximum of max profit or current position's max profit
        max_profit = max(max_profit, max_profit_sell_today)
        # assign min price to the minimum of price at current position or min price
        min_price_so_far = min(min_price_so_far, price)

    return max_profit
    # The time complexity is O(n) and the space complexity is O(1), where n is the length of the array.

prices = [310,370,215,275,280,260,260,230,230,230]
print(buy_and_sell_stock_once(prices))

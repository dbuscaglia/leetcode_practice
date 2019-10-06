
'''
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
        	return 0
        min_price = prices[0] 
        max_profit = 0
        for i in range(1, len(prices)):
        	p = prices[i]
        	if p < min_price:
        		min_price = p
        	else:
        		if max_profit < p - min_price:
        			max_profit = p - min_price
        return max_profit

assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0
assert Solution().maxProfit([7,2,5,2,7,2,9,1,3]) == 7 
assert Solution().maxProfit([1,2]) == 1
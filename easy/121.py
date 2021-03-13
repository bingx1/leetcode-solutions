class Solution:
    def maxProfit(self, prices):
	maxProfit, buy  = 0, prices[0]
	for price in prices:
	    if price <= buy:
		buy = price
		sell = float('-inf')
	    else:
		maxProfit = max(maxProfit, price - buy)
	return maxProfit

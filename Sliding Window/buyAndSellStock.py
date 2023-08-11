# LEETCODE LIST : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        l,r = 0,1

        while r < len(prices):
            if prices[l] < prices[r]:
                newprofit = max(profit,(prices[r]-prices[l]))
                profit = newprofit
            else:
                l = r
            r+=1
        return profit
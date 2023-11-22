# LINK : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/ 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                newProfit = prices[sell] - prices[buy]
                profit = max(newProfit,profit)
            else:
                buy = sell
                
            sell+=1

        return profit

# my solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        offers = []

        for i in prices:
            if i <= buy:
                buy = i
                sell = 0
                continue
            if i >= sell:
                sell = i
                offers.append(sell-buy)

        if offers:
            return max(offers)

        return 0


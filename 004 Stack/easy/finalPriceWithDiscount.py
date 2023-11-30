# LINK : https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
         stack = []
        
        for i in range(len(prices)):
            stack.append(prices[i])
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    stack[-1] = prices[i] - prices[j]
                    break
                    
        return stack 

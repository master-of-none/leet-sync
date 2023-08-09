class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP=0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            
            else:
                l = r
        
        return maxP
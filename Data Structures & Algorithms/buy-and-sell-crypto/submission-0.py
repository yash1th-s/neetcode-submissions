class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        ans = 0
        for p in prices:
            profit = p - bestBuy
            ans = max(ans,profit)
            bestBuy = min(bestBuy, p)
        return ans
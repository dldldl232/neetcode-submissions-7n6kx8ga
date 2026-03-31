class Solution:
    # return maximum profit
    # return 0 if max prof < 0
    def maxProfit(self, prices: List[int]) -> int:
        # we can do brute force 
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)

        return max_profit

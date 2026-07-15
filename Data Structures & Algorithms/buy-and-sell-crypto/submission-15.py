class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if exist return maximum profit 
        # else return 0

        """
        Possible ways: DP or sliding window
        """

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        
        return max_profit



        
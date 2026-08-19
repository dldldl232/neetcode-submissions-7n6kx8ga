class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0;
        int minP = prices[0]

        for (int& sell : prices) {
            maxP = max(maxP, sell - minP);
            minP = min(minP, sell);
        }

        return maxP;
    }
};

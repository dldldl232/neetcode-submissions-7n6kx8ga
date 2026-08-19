class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;

        for (int i = 0; i < prices.size(); ++i) {
            int initial_price = prices[i];
            // auto it = max_element(prices.begin()+i, prices.end());
            int max_sell_price = *max_element(prices.begin()+i, prices.end());
            int profit = max_sell_price - initial_price;

            if (profit > max_profit) {
                cout<<initial_price<<endl;
                cout<<max_sell_price<<endl;
                max_profit = profit;
            }
        }

        return max_profit;
    }
};

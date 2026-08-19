class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int end = prices.size();

        for (int i = 0; i < prices.size(); ++i) {
            int initial_price = prices[i];
            cout << "prices: " << prices[i+1] << "sell: " << prices[end] << endl;
            int max_sell_price = max(prices[i+1], prices[end]);
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

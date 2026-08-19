class Solution {
public:
    int maxArea(vector<int>& heights) {
        int amount = 0;
        int j = heights.size() - 1;
        int i = 0;

        while (i < j) {
            // we are getting the maximum possible height of the square
            int max_height = min(heights[i], heights[j]);
            int curr_amount = (j - i) * max_height;
            amount = max(amount, curr_amount);
            
            if (heights[i] < heights[j]) {
                ++i;
            } else {
                --j;
            }
        }

        return amount;
    }
};

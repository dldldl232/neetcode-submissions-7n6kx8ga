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

            if (curr_amount > amount) {
                amount = curr_amount;
            }
            
            if (heights[i+1] > heights[i]){
                ++i;
            } else if (heights[j-1] > heights[j]) {
                --j;
            } else {
                return amount;
            }

            // ++i;
            // --j;
        }

        return amount;
    }
};

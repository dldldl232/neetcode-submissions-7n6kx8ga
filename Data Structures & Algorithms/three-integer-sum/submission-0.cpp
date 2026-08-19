class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector <vector<int>> output;
        if (nums.size() < 3) return {};
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int target = -nums[i];
            int j = i + 1;
            int k = int(nums.size()) - 1;

            while (j < k) {
                if (nums[j] + nums[k] == target) {
                    output.push_back({nums[i], nums[j], nums[k]});
                    ++j;
                    --k;

                    while (j < k && nums[j] == nums[j - 1]) ++j;
                    while (j < k && nums[k] == nums[k + 1]) --k;
                    
                } else if (nums[j] + nums[k] > target) {
                    --k;
                } else {
                    ++j;
                }
            }
        }
        return output;
    }
};

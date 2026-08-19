class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        
        while (l < r) {
            int m = l + (r-1) / 2 //to prevent overflow for big l and r
            if (nums[mid] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return num[l];
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() -1;
        
        if (nums.size() == 1) {
            if (nums[l] == target) {
                return l;
            } else {
                return -1;
            }
        } 
        
        while (l <= r) {
            int m = l + (r - l) / 2;
            // if the left side is the group with bigger numbers
            // But what if the target is a big number or small number
            if (nums[m] == target) return m;

            // left side is sorted & ascending order
            if (nums[l] <= nums[m]) {
                // target is smaller than the smallest value on leftside
                // so must be on the right
                // the other condition is when target is on right side
                if (nums[l] > target || target > nums[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else {
                // right side is sorted
                if (nums[r] < target || target < nums[m]) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }

        return -1;
    }
};

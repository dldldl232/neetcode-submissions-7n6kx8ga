class Solution {
public:
    int search(vector<int>& nums, int target) {

        while (l < r) {
            int l = 0, r = nums.size() -1;
            int m = l + (r -l) / 2;
            cout << (r - 1) / 2 << endl;
            // if the left side is the group with bigger numbers
            // But what if the target is a big number or small number
            if (nums[m] == target) return m;

            if (nums[m] > target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }
};

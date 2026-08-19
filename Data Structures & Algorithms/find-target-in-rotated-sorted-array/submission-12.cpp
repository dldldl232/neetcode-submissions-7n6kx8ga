class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() -1;

        while (l <= r) {
            int m = l + (r -l) / 2;
            cout << "LEFT: " << l << endl;
            cout << "RIGHT:  " << r << endl;
            cout << m << endl;
            // if the left side is the group with bigger numbers
            // But what if the target is a big number or small number
            if (nums[m] == target) return m;

            if (nums[m] > target) {
                if (nums[m] < nums[r]) {
                    r = m;
                } else {
                    l = m + 1;
                }
            } else if (num[m] < target) {
                if (nums[m] < nums[r]) {
                    l = m + 1;
                } else if (nums[m] > nums[r]) {
                    r = m;
                }
            }
        }

        return -1;
    }
};

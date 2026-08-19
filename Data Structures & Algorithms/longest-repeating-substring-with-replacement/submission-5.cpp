class Solution {
public:
    int characterReplacement(string s, int k) {
        // sliding window problem
        int l = 0, count = 0;
        
        for (int r = 0; r < s.size(); ++r) {

            if (s[l] == s[r]) {
                cout << count << endl;
                ++count;
            } else if (k > 0 and s[l] != s[r]) {
                --k;
                s[r] = s[l];
                ++count;
            } else if (k < 0 and s[l] != s[r]) {
                return count;
            }
        }
        return count;
    }
};

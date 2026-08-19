class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> myset;
        int l = 0, output = 0;

        for (int r = 0; r < (int)s.size(); ++r) {
            while (myset.count(s[r])) { // duplicate found -> shrink
                myset.erase(s[l]);
                ++l;
            }
            myset.insert(s[r]);
            output = max(output, r - l + 1);
        }
        return output;
    }
};

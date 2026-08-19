class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> mapping = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c : s) {
            if (mapping.count(c)) {
                if (!stk.empty() && mapping[c] == stk.top()) {
                    stk.pop();
                } else {
                    return false;
                }
            } else {
                stk.push(c);
            }
        }

        return stk.empty();
    }
};

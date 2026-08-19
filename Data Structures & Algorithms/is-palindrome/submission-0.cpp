class Solution {
public:
    bool isPalindrome(string s) {
        std::stack<char> charStack;

        for (char c : s) {
            if (isalpha(c)) {
                charStack.push(tolower(c));
            }
        }

        for (char c : s) {
            if (isalpha(c)) {
                if(tolower(c) != charStack.top()) {
                    return false;
                }
                charStack.pop();
            }
        }

        return true;
    }
};

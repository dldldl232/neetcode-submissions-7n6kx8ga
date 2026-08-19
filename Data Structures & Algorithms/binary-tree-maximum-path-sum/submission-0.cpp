/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int globalMax = INT_MIN;

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return globalMax;
    }

    int dfs(TreeNode* root) {
        if (root == nullptr) return 0;

        int leftValue = max(0, dfs(root->left));
        int rightValue = max(0, dfs(root->right));

        int valueOfPath = root->val + leftValue + rightValue;
        globalMax = max(globalMax, valueOfPath);

        return root->val + max(leftValue, rightValue);


    }
};

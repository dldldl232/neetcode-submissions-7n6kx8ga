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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> output;
        treeList(root, output);
        return output[k-1];
    }

    void treeList(TreeNode* root, vector<int>& result) {
        if (!root) return;

        treeList(root->left, result);
        result.push_back(root->val);
        treeList(root->right, result);
    }
};


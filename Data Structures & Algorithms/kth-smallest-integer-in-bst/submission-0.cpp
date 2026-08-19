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
        vector<int> result = treeList(root, output);
        return result[k-1];
    }

    vector<int> treeList(TreeNode* root, vector<int>& result) {
        if (!root) return result;

        if (root->left && root->left->left == nullptr) {
            result.push_back(root->left->val);
        }
        result.push_back(root);
        if (root->right && root->right->right == nullptr) {
            result.push_back(root->right->val);
        }
        
        return treeList(root->left, result) && treeList(root->right, result);
    }
};


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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // if both trees are empty
        if (p == nullptr && q == nullptr) return true;

        queue<pair<TreeNode*, TreeNode*>> queue;
        queue.push({p, q});

        while (!queue.empty()) {
            //auto lets compiler deduce that its a treenode
            //using [ ] allows compiler to know that we are
            //unpacking the elemnts
            //if we used { } instead it would mean that we would be
            //initializing the pair
            auto [node1, node2] = queue.front();
            queue.pop();

            if (!node1 && !node2) continue; // means both are empty
            if (!node1 || !node2) return false; // if either are empty
            if (node1->val != node2->val) return false;

            queue.push({node1->left, node2->left});
            queue.push({node2->right, node2->right});
        }

        return true;
        
    }
};

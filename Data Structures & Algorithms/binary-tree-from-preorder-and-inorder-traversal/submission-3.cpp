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
    // global so we track the possition in pre arra
    int preIdx = 0;

    // since looping would take a lot of time
    // we use hash map to store val - pos
    unordered_map<int, int> inorderMap;

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // fill inorderMap
        for (int i = 0; i < inorder.size(); ++i) {
            inorderMap[inorder[i]] = i;
        }

        //arrayToTree function
        return arraytoTree(preorder, 0, inorder.size()-1);
    }

    TreeNode* arraytoTree(vector<int>& preorder, int left, int right) {
        // base case
        if (left > right) {
            return nullptr;
        }

        int rootVal = preorder[preIdx]; //store root val
        preIdx++; // move to the right

        //create new tree with root
        TreeNode* root = new TreeNode(rootVal);

        // Now we will process left and right through inorder
        // first get mid value which is the root
        int mid = inorderMap[rootVal]; // we stored the pos for each value

        root->left = arraytoTree(preorder, left, mid-1);

        root->right = arraytoTree(preorder, mid + 1, right);

        return root;
    }


};

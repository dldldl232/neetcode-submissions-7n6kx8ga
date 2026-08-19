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
#include <ranges>

class Codec {
public:

    // Encodes a tree to a single string.
    // converting an in-memory structure into a sequence of bits
    string serialize(TreeNode* root) {
        vector<string> data;
        dfsSerialize(root, data);
        return join(res, ","); // since we have to return a string not container
        // return "1,2,3,N,N,5"  
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        //get string
        //convert string to tree 
        //root -> left -> right
        vector<string> vals = split(data, ',');
        int i = 0;
        return dfsSerialize(vals, i);
    }
private:
    //pre-order
    void dfsSerialize(TreeNode* node, vector<string>& res) {
        if (!node) {
            res.push_back("N");
            return;
        }

        res.push_back(node->val);
        dfsSerialize(node->left, res);
        dfsSerialize(node->right, res);
    }

    TreeNode* dfsDeserialize(vector<string>& data, int& i) {
        TreeNode* node = new TreeNode(data[i]);

        ++i;
        node->left = data[i];
        ++i;
        node->right = data[i];
        if (data[i] == null)
    }
    
};

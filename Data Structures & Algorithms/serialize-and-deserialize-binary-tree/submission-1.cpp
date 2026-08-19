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

class Codec {
public:

    // Encodes a tree to a single string.
    // converting an in-memory structure into a sequence of bits
    string serialize(TreeNode* root) {
        vector<string> data;
        dfsSerialize(root, data);
        return join(data, ","); // since we have to return a string not container
        // return "1,2,3,N,N,5"  
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        //get string
        //convert string to tree 
        //root -> left -> right
        if (data.empty()) return nullptr;
        vector<string> vals = split(data, ',');
        int i = 0;
        return dfsDeserialize(vals, i);
    }
private:
    //pre-order
    void dfsSerialize(TreeNode* node, vector<string>& res) {
        if (!node) {
            res.push_back("N");
            return;
        }

        res.push_back(to_string(node->val));
        // used to_string as node->val is int. 
        dfsSerialize(node->left, res);
        dfsSerialize(node->right, res);
    }

    TreeNode* dfsDeserialize(vector<string>& data, int& i) {
        if (i >= data.size() || data[i] == "N") {
            i++;
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(data[i]));
        //we have to use stoi cause eve though we use indicies the value
        //is a string object
        i++;
        node->left = dfsDeserialize(data, i);
        //don't have to do ++i here cause the recursion moves the i itsself.
        node->right = dfsDeserialize(data, i);
        return node;

    }

    vector<string> split(const string &s, char delim) {
        vector<string> elems;
        stringstream ss(s);
        string item;
        while (getline(ss, item, delim)) {
            elems.push_back(item);
        }
        return elems;
    }

    string join(const vector<string> &v, const string &delim) {
        ostringstream s;
        for (const auto &i : v) {
            if (&i != &v[0])
                s << delim;
            s << i;
        }
        return s.str();
    }

};
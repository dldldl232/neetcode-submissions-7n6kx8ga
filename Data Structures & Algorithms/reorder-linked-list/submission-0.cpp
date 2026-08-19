/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* prev;
        ListNode* curr = head;
        int count = 0;

        while (head -> next != nullptr) {
            if (count == 0) {
                head = curr;
                curr = curr -> next;
                ++count;
            } else if (count % 2 != 0) {
                prev = curr;
                head -> next = curr -> next; 
                ++count;
            } else {
                head -> next = prev;
                ++count;
            }
        }
        
    }
};

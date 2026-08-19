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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* ctr = head;
        int count = 0;

        while (ctr) {
            count++;
            ctr = ctr -> next;
        }
        
        ListNode* temp = head;
        ListNode* prev = nullptr;
        int remove_pos = count - n;
        for (int i = 0; i < count; ++i) {
            if (i == remove_pos) {
                if (prev == nullptr) {
                    ListNode* newHead = temp -> next;
                    return newHead;
                } else {
                    prev -> next = temp -> next;
                    return head;
                }
            }
            prev = temp;
            temp = temp -> next;
        }

        return head;
    }
};

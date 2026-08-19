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
        // 1) Find middle (slow ends at midpoint for odd length)
        // ListNode* slow = head;
        // ListNode* fast = head;  // head or head->next both work
        // while (fast && fast->next) {
        //     slow = slow->next;
        //     fast = fast->next->next;
        // }

        // // 2) Split and reverse the second half
        // ListNode* second = slow->next;
        // slow->next = nullptr;       // cut
        // ListNode* prev = nullptr;
        // while (second) {
        //     ListNode* nxt = second->next;
        //     second->next = prev;
        //     prev = second;
        //     second = nxt;
        // }

        // // 3) Merge two halves
        // ListNode* first = head;
        // second = prev;
        // while (second) {            // second is never longer than first
        //     ListNode* t1 = first->next;
        //     ListNode* t2 = second->next;
        //     first->next = second;
        //     second->next = t1;
        //     first = t1;
        //     second = t2;
        // }
        if (!head || !head->next) return;

        ListNode* slow = head;
        ListNode* fast = head -> next;
        while (fast && fast -> next) {
            slow = slow -> next;
            fast = fast -> next -> next;            
        }

        ListNode* second = slow -> next;
        slow -> next = nullptr;
        ListNode* prev = nullptr;

        // reverse second half
        while (second) {
            ListNode* nxt = second -> next;
            second -> next = prev;
            prev = second;
            second = nxt;
        }

        // merge two half
        ListNode* first = head;
        second = prev;

        while (second) {
            ListNode* t1 = first -> next;
            ListNode* t2 = second -> next;
            first -> next = second;
            second -> next = t1;
            first = t1;
            second = t2;
        }
    }
};

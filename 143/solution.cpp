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
        if(head == nullptr || head->next == nullptr)
        {
            return;
        }
        // get to the middle of the lists using slow and fast pointer technique
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        while(fast != nullptr && fast->next != nullptr)
        {
            prev = slow; // so we can disconnect the lists to prevent cycle
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = nullptr;
        // reverse the second half the list
        prev = nullptr;
        ListNode* curr = slow;
        while(curr != nullptr)
        {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        while(prev != nullptr)
        {
            ListNode* tmp = head->next;
            head->next = prev;
            head = prev;
            prev = tmp;
        }
    }
};

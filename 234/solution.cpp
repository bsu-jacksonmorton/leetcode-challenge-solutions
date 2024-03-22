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
    bool isPalindrome(ListNode* head) {
        if(head->next == nullptr)
        {
            return true;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        // fast and slower pointer to find middle node in the list
        while(fast != nullptr && fast->next)
        {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = nullptr;
        prev = nullptr;
        ListNode* curr = slow;
        // reverse second half of the linked list
        while(curr)
        {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        // iterate through both the first half and second half of the lists comparing each node
        while(prev != nullptr && head != nullptr)
        {
            if(prev->val != head->val)
            {
                return false;
            }
            prev = prev->next;
            head = head->next;
        }
        // by default we assume palindrome and we failed to prove otherwise... so its a palindrome.
        return true;
    }
};

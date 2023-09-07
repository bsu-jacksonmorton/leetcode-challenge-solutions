# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case single element list or l==r gotcha
        if left==right or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        tmp = dummy
        for _ in range(left - 1):
            tmp = tmp.next
        prev, next = None, None
        curr = tmp.next
        eol = curr
        for _ in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        tmp.next = prev
        eol.next = curr
        return dummy.next

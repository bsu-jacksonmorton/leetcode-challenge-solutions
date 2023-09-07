# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        # step 1: iterate to the node just before node "left"
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        # step 2: reverse the list from left node to right node using stack
        s = []
        curr = prev.next
        print(right-left+1)
        for i in range(right - left + 1):
            s.append(curr)
            curr = curr.next
        while s:
            prev.next = s.pop()
            prev = prev.next
        # step 3: connect the ends of the list
        prev.next = curr
        return dummy.next

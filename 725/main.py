# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_size(self, head: Optional[ListNode]):
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.get_size(head)
        numNodesPer = n // k
        outliers = n % k
        res = []
        curr = head        
        for i in range(k):
            res.append(curr)
            for j in range(numNodesPer - (0 if outliers > 0 else 1)):
                if curr:
                    curr = curr.next
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp
            outliers -= 1
        return res

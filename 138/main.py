class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        while curr:
            tmp = Node(x=curr.val, next=curr.next, random=curr.random)
            curr.next = tmp
            curr = tmp.next
        curr = head.next
        dummy = curr
        while curr:
            if curr.next:
                curr.next = curr.next.next
            if curr.random:
                curr.random = curr.random.next
            curr = curr.next
        return dummy

# runtime: O(n)
# space: O(1)
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [float('inf'), -1]
        prev = None
        curr = head
        prev_crit_pos = -1 # used to determine the min
        first_crit_pos = -1 # used to find the max
        i = 0
        while curr.next:
            if prev:
                # check if local minima
                if prev.val > curr.val and curr.next.val > curr.val:
                    if prev_crit_pos != -1:
                        res[0] = min(abs(prev_crit_pos - i), res[0])
                    else:
                        first_crit_pos = i
                    prev_crit_pos = i
                # check if local maxima
                elif prev.val < curr.val and curr.next.val < curr.val:
                    if prev_crit_pos != -1:
                        res[0] = min(abs(prev_crit_pos - i), res[0])
                    else:
                        first_crit_pos = i
                    prev_crit_pos = i
            prev = curr
            curr = curr.next
            i += 1
        if first_crit_pos == -1 or prev_crit_pos == -1 or prev_crit_pos == first_crit_pos:
            return [-1, -1]
        res[1] = prev_crit_pos - first_crit_pos
        return res
            
        



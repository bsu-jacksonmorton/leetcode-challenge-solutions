class Solution:
    '''
    Runtime: O(n)
    Space: O(1)
    '''
    def maxDepth(self, s: str) -> int:
        ans = 0
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                ans = max(ans, count)
                count -= 1
        return ans

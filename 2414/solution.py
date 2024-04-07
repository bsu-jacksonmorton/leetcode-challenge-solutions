class Solution:
    '''
    runtime: O(n)
    space: O(1)
    '''
    def longestContinuousSubstring(self, s: str) -> int:
        start = 0
        ans = 0
        for end in range(1, len(s)):
            c = s[end]
            ans = max(end - start, ans)
            if ord(c) != ord(s[end-1]) + 1:
                start = end
        ans = max(len(s) - start, ans)
        return ans

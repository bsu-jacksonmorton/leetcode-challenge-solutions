class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        m = [-1] * 26
        for i in range(len(s)):
            key = ord(s[i]) - ord('a')
            if m[key] == -1:
                m[key] = i
            else:
                res = max(res, i - m[key] - 1)
        return res

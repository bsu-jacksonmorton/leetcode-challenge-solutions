class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = [0] * 26
        for c in s:
            letters[ord(c)-97] += 1
        for c in t:
            letters[ord(c)-97] -= 1
        for num in letters:
            if num:
                return False
        return True

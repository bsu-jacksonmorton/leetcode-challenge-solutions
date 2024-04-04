class Solution:
    '''
    Runtime: O(n)
    Space: O(26)
    '''
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        bank = [0] * 26
        for c in magazine:
            bank[ord('a') - ord(c)] += 1
        for c in ransomNote:
            if bank[ord('a') - ord(c)] == 0:
                return False
            bank[ord('a') - ord(c)] -= 1
        return True

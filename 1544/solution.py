class Solution:
    '''
    runtime: O(n)
    space: O(n) // we use a stack (ans) as auxiliary space
    '''
    def makeGood(self, s: str) -> str:
        ans = []
        for c in s:
            if len(ans) and abs(ord(ans[-1]) - ord(c)) == 32:
                ans.pop() 
            else:
                ans.append(c)
        return ''.join(ans)

class Solution:
    '''
    greedy monotonic stack
    runtime: O(n)
    space: O(n)
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        ans = [num[0]]
        for i in range(1, len(num)):
            curr = num[i]
            # we want the most significant digits to be the lowest numbers.
            while ans and ans[-1] > curr and k:
                ans.pop()
                k -= 1
            ans.append(curr)
        while k:
            ans.pop()
            k -= 1
        ans = ''.join(d for d in ans)
        ans = ans.lstrip('0')
        return ans if ans != "" else "0"

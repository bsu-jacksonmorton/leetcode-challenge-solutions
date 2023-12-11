class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        i = 1
        while n > 0:
            if i <= n:
                ans += 1
            n -= i
            i += 1
        return ans

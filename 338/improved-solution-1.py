class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1] * (n + 1)
        def count(n: int):
            res = 0
            while n > 0:
                if dp[n] != -1:
                    return dp[n] + res
                if n % 2:
                    res += 1
                n = n // 2
            return res
        for i in range(n+1):
            dp[i] = count(i)
        return dp

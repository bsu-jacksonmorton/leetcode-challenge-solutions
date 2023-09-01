class Solution:
    def count(self, n: int):
        res = 0
        while n > 0:
            if n % 2:
                res += 1
            n = n // 2
        return res
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n+1):
            res[i] = self.count(i)
        return res

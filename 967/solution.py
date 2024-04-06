
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = set()
        for i in range(1, 10):
            self.backtrack(i, n, k)
        return list(self.ans)
    def backtrack(self, curr, n, k):
        if len(str(curr)) == n:
            self.ans.add(curr)
            return
        last = curr % 10
        tmp = last + k
        curr = curr * 10
        if(0 <= tmp <= 9):
            curr += tmp
            self.backtrack(curr, n, k)
            curr -= tmp
        tmp = last - k
        if(0 <= tmp <= 9):
            curr += tmp
            self.backtrack(curr, n, k)
            curr -= tmp

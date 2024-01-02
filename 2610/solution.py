class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        rows_needed = max(counts.values())
        res = [[] for _ in range(rows_needed)]
        for c in counts:
            while counts[c] > 0:
                res[counts[c] - 1].append(c)
                counts[c] -= 1
        return res

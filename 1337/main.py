class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = list(range(len(mat)))
        res.sort(key=lambda x: mat[x].count(1))
        return res[:k]

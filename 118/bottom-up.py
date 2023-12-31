class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res
        for i in range(2, numRows):
            currRow = [1] * (i+1)
            for j in range(1, i):
                currRow[j] = res[i-1][j-1] + res[i-1][j]
            res.append(currRow)
        return res

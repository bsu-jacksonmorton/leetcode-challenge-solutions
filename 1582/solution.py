class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])
        row_counts = [0] * ROWS
        col_counts = [0] * COLS
        ans = 0

        # create our counts
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j]:
                    row_counts[i] += 1
                    col_counts[j] += 1

        # determine our special positions
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] and row_counts[i] == 1 and col_counts[j] == 1:
                    ans += 1
        return ans
        

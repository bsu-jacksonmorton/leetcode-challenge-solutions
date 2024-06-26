class Solution:
    '''
    DFS approach
    runtime: O(n * m)
    space: O(n * m) 
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if grid[row][col] == "1":
                grid[row][col] = "-1"
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)
        return ans

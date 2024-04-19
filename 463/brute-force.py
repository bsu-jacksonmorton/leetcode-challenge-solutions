class Solution:
    '''
    Brute Force Solution
    runtime: O(n * m)
    space: O(1)
    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                # check top
                if row - 1 < 0 or grid[row-1][col] == 0:
                    ans += 1
                # check bottom
                if row + 1 >= ROWS or grid[row+1][col] == 0:
                    ans += 1
                # check left
                if col - 1 < 0 or grid[row][col-1] == 0:
                    ans += 1
                # check right
                if col + 1 >= COLS or grid[row][col+1] == 0:
                    ans += 1
        return ans

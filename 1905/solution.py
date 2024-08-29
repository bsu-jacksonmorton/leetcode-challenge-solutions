class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        island = []
        def dfs(i,j):
            if 0 <= i < len(grid1) and 0 <= j < len(grid2[0]):
                if grid2[i][j] != 1:
                    return
                grid2[i][j] = -1
                island.append((i,j))
                # check up
                dfs(i-1, j)
                # check down
                dfs(i+1, j)
                # check left
                dfs(i, j-1)
                # check right
                dfs(i, j+1)
            
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                is_sub_island = True
                if grid2[row][col] == 1:
                    # explore the island
                    dfs(row,col)
                    # check if island in grid1
                    for i, j in island:
                        if grid1[i][j] != 1:
                            is_sub_island = False
                            break
                    if is_sub_island: res += 1
                    island.clear()
        return res

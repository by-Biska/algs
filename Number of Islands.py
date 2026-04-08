grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]

from typing import List

class Solution:
    def numberOfIslands(self, grid: List[List[str]]) -> int:
        raws = len(grid)
        cols = len(grid[0])
        totalislands = 0
        for i in range(raws):
            for j in range(cols):
                if int(grid[i][j]) == 1:
                    totalislands += 1
                    self.visit_is_island_DFS(grid, i, j)
        return totalislands
    def visit_is_island_DFS(self, grid, x, y):
        if x < 0  or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"

        self.visit_is_island_DFS(grid, x + 1, y)
        self.visit_is_island_DFS(grid, x, y + 1)
        self.visit_is_island_DFS(grid, x, y - 1)
        self.visit_is_island_DFS(grid, x -1 , y)

sol = Solution()
print(sol.numberOfIslands(grid))
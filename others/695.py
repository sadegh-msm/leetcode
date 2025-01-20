class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def find(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            return 1 + find(i-1, j) + find(i, j-1) + find(i, j+1) + find(i+1, j)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j]:
                    res = max(res, find(i, j))

        return res

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def find(i, j):
            if i >= rows or j >= cols:
                return 0
            if grid[i][j] == "0":
                return 0
            if i < 0 or j < 0:
                return 0

            grid[i][j] = "0"

            return 1 + find(i, j-1) + find(i, j+1) + find(i-1, j) + find(i+1, j)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1":
                    tmp = find(i, j)
                    if tmp != 0:
                        res += 1

        return res


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[m-1])

        left = 0
        right = m*n -1

        while left <= right:
            mid = left + (right-left)//2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            right = mid - 1

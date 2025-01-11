class Solution:
    def numTilings(self, n: int) -> int:
        arr = [1, 2, 5] + [0] * n
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        for i in range(3, n):
            arr[i] = (2 * arr[i-1] + arr[i-3]) % 1_000_000_007

        return arr[n-1]

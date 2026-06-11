class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # down[i][j] stores paths entering cell (i, j) moving DOWN
        # right[i][j] stores paths entering cell (i, j) moving RIGHT
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        
        # Base case: Robot starts at (0, 0)
        down[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                # Calculate paths coming from above into (i, j)
                if i > 0:
                    if grid[i-1][j] == 0:
                        down[i][j] = (down[i-1][j] + right[i-1][j]) % MOD
                    else:
                        down[i][j] = right[i-1][j]
                
                # Calculate paths coming from the left into (i, j)
                if j > 0:
                    if grid[i][j-1] == 0:
                        right[i][j] = (down[i][j-1] + right[i][j-1]) % MOD
                    else:
                        right[i][j] = down[i][j-1]
                        
        # Total paths reaching the destination
        return (down[m-1][n-1] + right[m-1][n-1]) % MOD
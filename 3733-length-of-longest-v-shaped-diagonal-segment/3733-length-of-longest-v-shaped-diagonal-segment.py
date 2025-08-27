

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Diagonal directions: NE, SE, SW, NW
        DIRS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @lru_cache(None)
        def dfs(i: int, j: int, turned: int, expect: int, d: int) -> int:
            # out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            # must match the expected value (2, then 0, then 2, ...)
            if grid[i][j] != expect:
                return 0

            # continue straight
            di, dj = DIRS[d]
            next_expect = 0 if expect == 2 else 2
            best = 1 + dfs(i + di, j + dj, turned, next_expect, d)

            # one optional clockwise turn to keep the "V" shape
            if turned == 0:
                nd = (d + 1) % 4
                ndi, ndj = DIRS[nd]
                best = max(best, 1 + dfs(i + ndi, j + ndj, 1, next_expect, nd))

            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d, (di, dj) in enumerate(DIRS):
                        ans = max(ans, 1 + dfs(i + di, j + dj, 0, 2, d))
        return ans

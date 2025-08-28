class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * n for _ in range(n)]
        diag = defaultdict(list)  # key = i - j for TL↘BR diagonals

        # collect values per diagonal
        for i in range(n):
            for j in range(n):
                diag[i - j].append(grid[i][j])

        # sort each diagonal:
        #   keys < 0 (below main)  -> non-increasing
        #   keys >= 0 (on/above)   -> non-decreasing
        for key, arr in diag.items():
            arr.sort(reverse=(key < 0))

        # rebuild matrix by popping from the tail
        for i in range(n):
            for j in range(n):
                ans[i][j] = diag[i - j].pop()

        return ans
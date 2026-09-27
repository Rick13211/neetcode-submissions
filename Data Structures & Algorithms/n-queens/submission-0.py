class Solution:
    def isPossible(self, r, c):
        for row in range(r):
            col = self.rows[row]

            if col == c:
                return False

            if abs(r - row) == abs(c - col):
                return False

        return True

    def formBoard(self, rows):
        board = [['.'] * self.n for _ in range(self.n)]

        for i in range(len(rows)):
            board[i][rows[i]] = 'Q'

        ans = ["".join(row) for row in board]
        return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.rows = [-1] * n
        res = []

        def dfs(r):
            if r == n:
                board = self.formBoard(self.rows)
                res.append(board)
                return

            for c in range(n):
                if self.isPossible(r, c):
                    self.rows[r] = c

                    dfs(r + 1)

                    self.rows[r] = -1

        dfs(0)
        return res
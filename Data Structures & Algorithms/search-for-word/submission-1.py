from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c, idx):
            if idx == len(word):
                return True
                
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#' 
            for dr, dc in directions:
                if dfs(r + dr, c + dc, idx + 1):
                    return True
            
            board[r][c] = temp
            return False
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False

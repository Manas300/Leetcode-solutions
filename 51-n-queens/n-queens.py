from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]  # empty board

        # Check if a queen can be placed at (row, col)
        def is_safe(row, col):
            # Check column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check upper-left diagonal
            r, c = row-1, col-1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row-1, col+1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True  # safe to place queen

        # Backtracking function: try to place queens row by row
        def backtrack(row):
            # Base case: all rows filled
            if row == n:
                # Convert board to string format and save
                result.append(["".join(r) for r in board])
                return

            # Try placing queen in each column
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"   # place queen
                    backtrack(row + 1)      # recurse to next row
                    board[row][col] = "."   # remove queen (backtrack)

        backtrack(0)  # start from first row
        return result

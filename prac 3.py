class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]  # Initialize the board with 0s

    def print_board(self):
        for row in self.board:
            print(" ".join("Q" if col else "." for col in row))  # Print 'Q' for queen, '.' for empty
        print()  # Blank line after the board for readability

    def is_safe(self, row, col):
        # Check this row on the left side
        for i in range(col):
            if self.board[row][i]:
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        return True

    def solve_n_queens_util(self, col):
        # If all queens are placed
        if col >= self.n:
            return True

        # Try placing this queen in all rows one by one
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1  # Place the queen

                # Recursively place the rest of the queens
                if self.solve_n_queens_util(col + 1):
                    return True

                self.board[i][col] = 0  # Backtrack if placing the queen here doesn't lead to a solution

        return False

    def solve(self):
        if not self.solve_n_queens_util(0):
            print("Solution does not exist")
            return False
        self.print_board()
        return True

# Example usage:
n = 4
n_queens = NQueens(n)
n_queens.solve()

class Solution:
    def solveNQueens(self, n):
        initial_pos = [n * "." for _ in range(n)]
        pos_dict = {i: initial_pos[i][:i] + "Q" + initial_pos[i][i + 1:] for i, val in enumerate(initial_pos)}
        positions = list(pos_dict.keys())
        subset, res = [], []

        def is_valid(row, col):
            for i in range(row):
                if subset[i] == col or abs(subset[i] - col) == row - i:
                    return False
            return True

        def backtrack(row):
            if row == n:
                res.append(subset[:])
                return
            for col in range(n):
                if is_valid(row, positions[col]):
                    subset.append(positions[col])
                    backtrack(row + 1)
                    subset.pop()

        backtrack(0)
        for i in range(len(res)):
            res[i] = [pos_dict[n] for n in res[i]]

        return res




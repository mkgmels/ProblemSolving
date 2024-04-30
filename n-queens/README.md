Sure, here's a README file for the N-Queens problem:

---

# N-Queens Problem

The N-Queens problem is a classic problem in computer science and combinatorial optimization. The problem is defined as follows: given an \( n \times n \) chessboard, place \( n \) queens on the board such that no two queens attack each other. In chess, a queen can attack horizontally, vertically, and diagonally.

## Solution Approach

The solution to the N-Queens problem can be efficiently found using backtracking, a general algorithmic technique that incrementally builds candidates for a solution, abandoning each partial candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. The backtracking algorithm for the N-Queens problem involves recursively exploring all possible queen placements on the board, ensuring that no two queens attack each other.

## Implementation

We have provided a Python implementation of the N-Queens problem using backtracking. The function `solveNQueens(n)` takes an integer `n` as input and returns all distinct solutions to the N-Queens puzzle for a board of size \( n \times n \). The solutions are represented as lists of strings, where each string represents a row of the chessboard, with 'Q' indicating the position of a queen and '.' indicating an empty space.

## Usage

To use the provided implementation, simply call the `solveNQueens(n)` function with the desired board size `n`. The function will return a list of all distinct solutions to the N-Queens problem for the given board size.

Example usage:

```python
print(Solution().solveNQueens(4))
print(Solution().solveNQueens(8))
```

## Constraints

- \( 1 \leq n \leq 9 \)



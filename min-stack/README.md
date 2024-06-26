# Problem: Design a Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

### Example:

```python
# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())      # Output: 0
print(minStack.getMin())  # Output: -2
```

### Constraints:

- $-2^{31} \leq \text{val} \leq 2^{31} - 1$
- Methods `pop`, `top`, and `getMin` operations will always be called on non-empty stacks.
- At most $3 \times 10^4$ calls will be made to `push`, `pop`, `top`, and `getMin`.

### Additional Resources:
- [Problem Description on LeetCode](https://leetcode.com/problems/min-stack/)
- [Submission on LeetCode](https://leetcode.com/problems/min-stack/submissions/1241136254)

### Solution:
The provided solution to this problem is implemented in the Python script `min-stack-submission.py` located inside the "solution" folder.

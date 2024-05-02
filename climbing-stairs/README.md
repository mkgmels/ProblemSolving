# Climbing Stairs

## Problem Statement

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Example

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## Constraints

1 <= n <= 45

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def fibonacci(n,res=[1,1],i=2):
            if n==0:
                return
            
            res.append(res[i-1]+res[i-2])
            fibonacci(n-1,res,i+1)
            return res[n]

        return fibonacci(n)
```

This solution utilizes a recursive approach based on the Fibonacci sequence to calculate the number of distinct ways to climb to the top of the staircase. It has a time complexity of O(n) and a space complexity of O(n), where n is the number of steps.

# Problem: Group Anagrams

Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples:

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

### Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

### Solution:
The provided solution to this problem involves using a hash map to group anagrams together. The Python script `group-anagram-submission.py` inside the "solution" folder implements this approach.

### Additional Resources:
For more details about the problem and to access the provided solution, refer to the following links:
- [Problem Description on LeetCode](./links/leetcode_problem_description.txt)
- [Submission on LeetCode](./links/leetcode_submission.txt)

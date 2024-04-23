class Solution:
    def isAnagram(self,s,t):
    # Check if lengths of s and t are different
        if len(s) != len(t):
            return False
        
        # Initialize dictionaries to store character counts
        count_s = {}
        count_t = {}
        
        # Count occurrences of each character in string s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        # Count occurrences of each character in string t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the two dictionaries
        return count_s == count_t




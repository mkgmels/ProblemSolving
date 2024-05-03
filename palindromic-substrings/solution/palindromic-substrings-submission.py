class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_fn(p1,p2,s):
            palindromes_count=0

            max_len,max_str=0,''
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                palindromes_count+=1
                p1-=1
                p2+=1

            return palindromes_count
        odd_palindromes,even_palindromes=0,0
        for i in range(len(s)):
            odd_palindromes+=expand_fn(i,i,s)
            even_palindromes+=expand_fn(i,i+1,s)
        total_count=odd_palindromes+even_palindromes
        return total_count      

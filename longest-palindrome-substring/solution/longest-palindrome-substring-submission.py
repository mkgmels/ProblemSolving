class Solution:
    def longestPalindrome(self, s):

        def expand_fn(p1,p2,s):

            max_len,max_str=0,''
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                if len(s[p1:p2+1])>max_len:
                    max_len=len(s[p1:p2+1])
                    max_str=s[p1:p2+1]
                p1-=1
                p2+=1
            return max_str
        result=''
        for i in range(len(s)):
            odd=expand_fn(i,i,s)
            even=expand_fn(i,i+1,s)
            if len(odd)>len(result):
                result=odd
            if len(even)>len(result):
                result=even
        return result

            
            

    


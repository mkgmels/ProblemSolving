class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        str1=list(s)
        str2=list(t)
        str1_counter,str2_counter={},{}
        for l in str1:
            if l not in str1_counter:
                str1_counter[l]=1
            else:
                str1_counter[l]+=1

        for l in str2:
            if l not in str2_counter:
                str2_counter[l]=1
            else:
                str2_counter[l]+=1 
        for l in str1:
            if l not in str2_counter:
                return False
            elif str1_counter[l]!=str2_counter[l]:
                return False
            else:
                continue;
        return True



        

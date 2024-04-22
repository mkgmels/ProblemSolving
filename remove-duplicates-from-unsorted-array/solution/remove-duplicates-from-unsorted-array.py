
class Solution:
    def removeDuplicate(self, A, N):
        counter={}
        i=0
        while i < len(A):
            n=A[i]
            if n not in counter:
                counter[n]=1
                i+=1
            elif counter[n]==1:
                A.pop(i)
        return A
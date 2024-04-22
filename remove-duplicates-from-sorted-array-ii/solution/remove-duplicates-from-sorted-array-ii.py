class Solution:
    def removeDuplicates(self, nums) -> int:
        counter={}
        i=0
        while i < len(nums):
            n=nums[i]
            if n not in counter.keys():
                counter[n]=1
                i+=1
            elif counter[n]<2:
                counter[n]+=1
                i+=1
            else:
                nums.pop(i)
        
        return len(nums)
            



class Solution:
    def permute(self, nums):
        #base case
        if nums==[]:
            return [[]]
        #recursive case
        permuatations=[]
        for i in range(len(nums)):
            current=nums[i]
            others=nums[:i]+nums[i+1:]
            for p in self.permute(others):
                permuatations.append([current]+p)
        return permuatations

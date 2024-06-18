class Solution:
    def subsetsWithDup(self, nums):
        #base case 
        if nums==[]:
            return [[]]
        #recursive case
        subsets=[[]]
        nums=sorted(nums)
        for i in range(len(nums)):
            current=nums[i]
            if [current] not in subsets:
                subsets.append([current])
            others=nums[i+1:]
            for s in self.subsetsWithDup(others):
                new_subset=[current]+s
                if new_subset not in subsets:
                    subsets.append(new_subset)

        return subsets

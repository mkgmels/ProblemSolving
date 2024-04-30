class Solution:
    def subsets(self,nums):
        subset,res=[],[]
        def backtrack(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            else:
                res.append(subset.copy())


            while i < len(nums):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
                i+=1

        backtrack(0)
        return res

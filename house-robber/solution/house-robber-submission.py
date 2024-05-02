class Solution:
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        dp=[]
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums),1):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
        return dp[-1]

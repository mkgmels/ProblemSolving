class Solution:
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        dp=[]
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)-1):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
        dp2=[]
        nums2=nums[1:]
        if len(nums2)==1:
            return max(dp[-1],nums2[0])
        dp2.append(nums2[0])
        dp2.append(max(nums2[0],nums2[1]))
        for i in range(2,len(nums2)):
            dp2.append(max(dp2[i-2]+nums2[i],dp2[i-1]))    
        return max(dp[-1],dp2[-1])

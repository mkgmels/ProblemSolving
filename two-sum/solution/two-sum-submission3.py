class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_nums=set()
        for i,n in enumerate(nums):
            if target-n  in comp_nums:
                comp_index=nums.index(target-n)
                return i,comp_index
            comp_nums.add(n)

                



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter={}
        for n in nums:
            if n not in counter:
                counter[n]=1
            elif counter[n]==1:
                return True
        return False

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1]*len(nums)
        prefix = nums[0]
        for i in range(1,len(nums)):
            sol[i] *= prefix
            prefix *= nums[i]
        
        sufix = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            sol[i] *= sufix
            sufix *= nums[i]
        
        return sol
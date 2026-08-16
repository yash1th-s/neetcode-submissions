class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            curr = nums[i]
            while l<r:
                if nums[l] + nums[r] == -(curr):
                    sol.append([curr, nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while r>l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -(curr):
                    l += 1
                else:
                    r -= 1
        return sol
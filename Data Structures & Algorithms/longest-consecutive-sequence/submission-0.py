class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for n in numSet:
            if n-1 not in numSet:
                count = 1
                while n+1 in numSet:
                    count += 1
                    n += 1
                ans = max(ans, count)
        return ans
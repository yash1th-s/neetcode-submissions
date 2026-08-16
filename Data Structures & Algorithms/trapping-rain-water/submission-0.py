class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        left_b = [0] * n
        leftMax = height[0]
        for i in range(1,n-1):
            left_b[i] = leftMax
            leftMax = max(leftMax, height[i])
        
        right_b = [0] * n
        rightMax = height[n-1]
        for i in range(n-2, -1, -1):
            right_b[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        for i in range(n):
            water = min(left_b[i], right_b[i]) - height[i]
            if water>0:
                ans += water
        return ans
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                idx,height = stack.pop()
                area = height * (i-idx)
                ans = max(ans, area)
                start = idx
            stack.append((start,h))

        for i,h in stack:
            area = h * (len(heights)-i)
            ans = max(ans, area)
        
        return ans
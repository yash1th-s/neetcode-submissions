class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            c = s[r]
            while c in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(c)
            ans = max(ans, r-l+1)
        return ans
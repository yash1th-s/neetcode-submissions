class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        freq = {}
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0)+1
            maxFreq = max(freq.values())
            while (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount, tCount = {}, {}
        for i in t:
            tCount[i] = tCount.get(i, 0)+1
        
        need, have = len(tCount), 0
        res, resLen = [-1,-1], float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            sCount[c] = sCount.get(c,0)+1
            if c in t and sCount[c] == tCount[c]:
                have += 1
                while need == have:
                    if r-l+1 < resLen:
                        res = [l, r]
                        resLen = r-l+1
                    sCount[s[l]] -= 1
                    if s[l] in t and sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                    l += 1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""

                
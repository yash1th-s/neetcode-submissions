class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re 
        clean_s = re.sub(r'[^A-Za-z0-9]','',s).lower()
        l,r = 0,len(clean_s)-1
        while l<r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        return True

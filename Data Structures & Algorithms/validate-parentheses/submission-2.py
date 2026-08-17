class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0 : return False

        par = {')':'(', '}':'{', ']':'['}

        stack = []

        for i in s:
            if i not in par:
                stack.append(i)
                continue
            if not stack or stack[-1] != par[i]:
                return False
            stack.pop()
        return True if not stack else False
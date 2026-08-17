class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+', '-', '*', '/')

        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
                continue
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        return stack[-1]
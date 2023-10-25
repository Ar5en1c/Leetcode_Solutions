class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            if i == '+':
                m = stack.pop()
                n = stack.pop()
                stack.append(m + n)
            if i == '-':
                m = stack.pop()
                n = stack.pop()
                stack.append(n - m)
            if i == '*':
                m = stack.pop()
                n = stack.pop()
                stack.append(m * n)
            if i == '/':
                m = stack.pop()
                n = stack.pop()
                stack.append(int(float(n) / m))
        return stack[0]
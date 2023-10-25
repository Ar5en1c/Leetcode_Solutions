class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        Map = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i not in Map:
                stack.append(i)
                continue
            if not stack or stack[-1] != Map[i]:
                return False
            stack.pop()

        return not stack
            # elif i == ')' or i == '}' or i == ']':
            #     stack.pop()
        
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
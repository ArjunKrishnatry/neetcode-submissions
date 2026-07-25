class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strlist = list(s)
        for i in strlist:
            if i == '[' or i =='{' or i == '(':
                stack.append(i)

            else:
                if not stack:
                    return False
                open_b = stack.pop()
                if i == ']' and open_b == '[':
                    continue
                elif i == '}' and open_b == '{':
                    continue
                elif i == ')' and open_b == '(':
                    continue
                else:
                    return False
        return len(stack) == 0
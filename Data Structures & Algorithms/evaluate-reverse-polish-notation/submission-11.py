class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        if len(tokens) == 1:
            return int(tokens[0])
        i = 0
        while tokens[i] not in operators:
            i += 1
        val1, val2 = int(tokens[i-2]), int(tokens[i-1])
        if tokens[i] == '+':
            val = val1 + val2
        elif tokens[i] == '-':
            val = val1 - val2
        elif tokens[i] == '*':
            val = val1 * val2
        elif tokens[i] == '/':
            val = int(val1 / val2)
        tokens[i] = str(val)
        del tokens[i-2:i]
        return self.evalRPN(tokens)
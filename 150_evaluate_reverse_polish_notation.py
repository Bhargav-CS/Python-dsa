class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
        return stack[0]
    
    
tokens = ["2", "1", "+", "3", "*"]
sol = Solution()
print(sol.evalRPN(tokens)) # 9
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        for i in x:
            if i in ['{', '(', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
                
        return not stack
    
# Example usage:
input = "{([])}"
print(Solution().ispar(input))  # Output: True
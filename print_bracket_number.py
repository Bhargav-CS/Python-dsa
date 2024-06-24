class Solution:
    def bracketNumbers(self, str):
        stack = []
        result = []
        count = 1
        
        for char in str:
            if char == '(':
                stack.append(count)
                result.append(count)
                count += 1
            elif char == ')':
                result.append(stack.pop())
        
        # return ' '.join(map(str, result))
        return result


    
# str = "(aa(bdc))p(dee)"
str = "(((()("
sol = Solution()
print(sol.bracketNumbers(str)) # 1 2 3 4 4 5

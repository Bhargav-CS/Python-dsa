class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for token in path.split('/'):
            if token == '..':
                if stack:
                    stack.pop()
            elif token and token != '.':
                stack.append(token)
        return '/' + '/'.join(stack)
    
        
    
path = "/home/"
sol = Solution()
print(sol.simplifyPath(path)) # /home
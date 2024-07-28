class Solution:
    def removeDups(self, str:str):
        hashmap = set()
        
        for char in str:
            if char not in hashmap:
                hashmap.add(char)
                print(char, end="")
                
        return ""
        
    
str = "zvvo"
sol = Solution()
print(sol.removeDups(str))

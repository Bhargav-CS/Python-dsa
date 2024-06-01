class Solution:    
    def oddEven(self, s : str) -> str:
        alphabates = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        hashmap = {}
        x = 0 
        
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for i in hashmap:
            if hashmap[i] % 2 == alphabates.index(i) % 2:
                x += 1
        
        if x % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
                
    
s = "nobitaa"
sol = Solution()
print(sol.oddEven(s))


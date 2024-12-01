class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        hashmap = {x:0 for x in s}

        for char in s:
            hashmap[char] += 1
            
        for key in hashmap:
            if hashmap.get(key) == 1:
                return key
        
        return "$"
    
s = "geeksforgeeks"
sol = Solution()
print(sol.nonRepeatingChar(s))

from typing import List

class Solution:
    def longestCommonPrefix(self, arr:List[str]):
        set_a = set()
        min_a = min(arr)
        
        while min_a:
            for ele in arr:
                ele = ele[:len(min_a)]
                set_a.add(ele)
                
            
            # print(set_a)
            if len(set_a) == 1:
                return min_a
            set_a.clear()
            min_a = min_a[:len(min_a) - 1]
                    
        return -1
            
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
# arr = ["hello", "world"]
sol = Solution()
print(sol.longestCommonPrefix(arr))


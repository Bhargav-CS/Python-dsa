from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0
        
        for strings in words:
            i = 0
            while i < len(strings):
                if allowed.find(strings[i]) != -1:
                    i += 1
                
                else:
                    i = 0
                    break
            
            if i > 0:
                count += 1

                    
                    
        return count
    
    
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]

sol = Solution()
print(sol.countConsistentStrings(allowed, words))

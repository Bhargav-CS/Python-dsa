class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())
    
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs)) # [["ate","eat","tea"],["nat","tan"],["bat"]]
        
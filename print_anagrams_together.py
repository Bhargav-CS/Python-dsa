from collections import defaultdict
class Solution:
    def anagrams(self, arr):
        mp = defaultdict(list)
        def makeSort(word):
            return ''.join(sorted(list(word)))
        
        for word in arr:
            mp[makeSort(word)].append(word)
        
        res = []
        for k in mp:
            res.append(mp[k])
        
        return res
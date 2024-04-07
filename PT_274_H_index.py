class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        tmp = [0 for _ in range(N+1)]
        for i, v in enumerate (citations):
            if v > N:
                tmp[N] +=1
            else:
                tmp[v] += 1

        total = 0

        for i in range(N, -1, -1):
            total += tmp[i]
            if total >= i:
                return i
            
# citations = [3,0,6,1,5]
citations = [3,1,2,3,2]
sol = Solution()
print(sol.hIndex(citations)) 
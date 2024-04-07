class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0] * (N+1)
        for citation in citations:
            count[min(citation, N)] += 1
        k = N
        s = count[N]
        while k > s:
            k -= 1
            s += count[k]
        return k 

N = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex(N)) # 3
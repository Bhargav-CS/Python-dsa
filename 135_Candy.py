class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        

        N = len(ratings)
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
        tmp = [1 for _ in range(N)]
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                tmp[i] = tmp[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                tmp[i] = max(tmp[i], tmp[i+1]+1)
        return sum(tmp)
    
ratings = [1,0,2]
sol = Solution()
print(sol.candy(ratings)) # 5

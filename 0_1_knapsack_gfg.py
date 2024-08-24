class Solution:
    def __init__(self):
        self.dp = []

    def dfs(self, w, wt, val, index, current_weight):
        if index >= len(val):
            return 0
        
        if self.dp[index][current_weight] is not None:
            return self.dp[index][current_weight]
        
        pick = 0
        if wt[index] + current_weight <= w:
            pick = val[index] + self.dfs(w, wt, val, index + 1, current_weight + wt[index])
        
        not_pick = self.dfs(w, wt, val, index + 1, current_weight)
        
        self.dp[index][current_weight] = max(pick, not_pick)
        return self.dp[index][current_weight]

    def knapSack(self, W, wt, val):
        self.dp = [[None] * (W + 1) for _ in range(len(val))]
        return self.dfs(W, wt, val, 0, 0)
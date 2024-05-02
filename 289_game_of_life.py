class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_neighbours = 0
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        live_neighbours += board[x][y] & 1
                if live_neighbours == 3 or live_neighbours - board[i][j] == 3:
                    board[i][j] |= 2
        for i in range(rows):
            for j in range(cols):
                board[i][j] >>= 1
        return board
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol = Solution()
print(sol.gameOfLife(board)) # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
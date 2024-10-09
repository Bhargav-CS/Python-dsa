class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None
        
def display(head):
    Dp = head
    
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        
        Dp = Dp.down
        
class Solution:

    def constructLinkedMatrix(self, mat):


        nodes = [[Node(x) for x in row] for row in mat]

        for i in range(len(mat)):

            for j in range(len(mat) - 1):

                nodes[i][j].right = nodes[i][j + 1]

                nodes[j][i].down = nodes[j + 1][i]

        return nodes[0][0]
        
    
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

sol = Solution()
head = sol.constructLinkedMatrix(mat)
if head is None:
    print(-1)
    
display(head)
print()


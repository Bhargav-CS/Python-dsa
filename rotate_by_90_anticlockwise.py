
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def reverse(self,arr):
        l,h=0,len(arr)-1
        while l<h:
            arr[l],arr[h]=arr[h],arr[l]
            l+=1
            h-=1
    
    def rotateby90(self, mat): 
        for row in mat:
            self.reverse(row)
        rows,cols=len(mat),len(mat[0])
        for i in range(rows):
            for j in range(i+1,cols):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

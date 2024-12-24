def searchMatrix(self, mat, x):
    rows,cols=len(mat),len(mat[0])
    l,h=0,rows*cols-1
    while l<=h:
        mid=(l+h)//2
        i,j=mid//cols,mid%cols
        if mat[i][j]==x:
            return True
        elif mat[i][j]>x:
            h=mid-1
        else:
            l=mid+1
    return False
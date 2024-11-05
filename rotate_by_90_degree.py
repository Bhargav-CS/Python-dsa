def rotate(mat): 
    #code here
    c=[[0]*len(mat[0]) for _ in range(len(mat))]
    s1=len(mat)
    s2=len(mat[0])
    for i in range(s1):
        for j in range(s2):
            c[i][j]=mat[s2-j-1][i]
    for i in range(s1):
        for j in range(s2):
            mat[i][j]=c[i][j]
    return mat
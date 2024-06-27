def isToepliz(mat):
    n , m = len(mat), len(mat[0])
    count = 0
    if n <=1 or m <= 1:
        return True
    
    for i in range(n):
        for j in range(m):
            if ((j+1) < m and (i+1) < n) and mat[i][j] == mat[i+1][j+1]:
                count +=1
            
    if count == (n-1) * (m-1):
        return True
    
    else:
        return False
    

# mat = [[6, 7, 8,],
#        [4, 6, 7],
#        [1, 4, 6]]

# mat = [[1, 2, 3],
#        [4, 5, 6]]

# mat = [[6, 7, 8, 9, 10],
#        [5, 6, 7, 1, 9],
#        [10, 5, 6, 7, 8]]

mat = [[1, 2, 3, 4, 5, 6, 7],
       [8, 1, 2, 3, 4, 5, 6],
       [9, 8, 1, 2, 3, 4, 5],
       [10, 9, 8, 1, 2, 2, 4],
       [11, 10, 9, 8, 1, 2, 3]]

print(isToepliz(mat))
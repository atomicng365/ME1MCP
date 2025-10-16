def matrix(A):
    for i in range(0,len(A)):
        print(A[i])

def MatVec(A,B):
    if len(A[0]) == len(B):
        for k in range(0,len(A)):
            for i in range(0,len(B)):
                (A[k][i]) = (A[k][i]*B[i][0])
        return A
    else:
        return 0
    
print(matrix(MatVec([[1,2,3],[2,3,4]],[[1],[2],[3]])))
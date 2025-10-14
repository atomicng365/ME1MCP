def matrix(A):
    for i in range(0,len(A)):
        print(A[i])

A = [[24,67,81],[10,3,28],[63,55,17]]
print(A)
(A[0][1],A[2][2]) = (A[2][2],A[0][1])
print(A)
(A[0][2],A[2][0]) = (A[2][0],A[0][2])
A[1][1] = 24+28
print(matrix(A))
def ReadMatrix(u,row,column):
    f = open(u,'r')
    a = f.readlines()
    f.close()
    matrix = []
    matrixs = []
    for item in a:
        matrix = matrix + [int(item)]
    for i in range(0,column):
        n = []
        for k in range(0,row):
            n = n + [matrix[i*row+k]]
        matrixs = matrixs + [n]
    return matrixs

A = ReadMatrix('MatA.txt',60,60)
B = ReadMatrix('MatB.txt',60,60)
C = []
for i in range(0,60):
    n = []
    for k in range(0,60):
        n = n + [A[i][k]+B[i][k]]
    C = C + [n]
print(C)




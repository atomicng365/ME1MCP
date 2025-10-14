def ReadMatrix(u,row,column):
    f = open(u,'r')
    a = f.readlines()
    f.close()
    matrix = []
    matrixs = []
    for item in a:
        matrix = matrix + [int(item)]
    for i in range(0,column-1):
        n = []
        for k in range(0,row-1):
            n = n + [matrix[i*row+k]]
        matrixs = matrixs + [n]
    return matrixs

print(ReadMatrix('MatA.txt',60,60))



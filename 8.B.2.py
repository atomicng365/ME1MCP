import math
def Matrix(A):
    Mat = []
    for k in range(0,A):
        a = []
        if math.fmod(k,2) == 0:
            for i in range(0,A):
                if math.fmod(i,2) == 0:
                    a = a + [1]
                elif math.fmod(i,2) == 1:
                    a = a + [0]
        elif math.fmod(k,2) == 1:
            for i in range(0,A):
                if math.fmod(i,2) == 0:
                    a = a + [0]
                elif math.fmod(i,2) == 1:
                    a = a + [1]
        Mat = Mat + [a]
    return Mat
n = 11
f = open('chessboard.txt','w')
f.write(str(len(Matrix(n)))+'\n')
f.write(str(len(Matrix(n)[0]))+'\n')
for i in range(0,n):
    for k in Matrix(n)[i]:
        f.write(str(k) + '\n')
f.close()




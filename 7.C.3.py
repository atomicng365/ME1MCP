def matrix(A):
    for i in range(0,len(A)):
        print(A[i])

N = int(input('N='))
matric = []

for i in range(0,N):
    matrics = []
    for m in range(0,N):
        matrics = matrics + [0]
    matric = matric + [matrics]

for i in range(0,N):
    matric[i][i] = 1
    matric[N-i-1][i] = 1

print(matrix(matric))

def Fib(N):
    if N == 1:
        return 1
    elif N > 1:
        return N*Fib(N-1)
    
print(Fib(4))
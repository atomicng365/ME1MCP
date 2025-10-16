N = 1

Q = int(input('Q='))
x = 0.8

def Y(y,n):
    if n > 0:
        return y**n + Y(y,n-1)
    elif n == 0:
        return 1

h = 1/10**Q

found = False
#recursion where +1 to N until the condition is met
while(not found):
    if abs(Y(x,N)- Y(x,N+1))<h:
        found == True
    else:
        N = N+1

print(N)
print(Y(x,N))


#while (not found):
    #if Bingo[count] == find:
        #found = True
    #else:
        #count = count + 1

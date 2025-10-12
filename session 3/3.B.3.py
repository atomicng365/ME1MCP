import random
r = random.randint(1,3)
u = input('What is your hand? R, P or S \n')
p = ''
if r == 1:
    p = 'R'
elif r == 2:
    p = 'P'
elif r == 3:
    p = 'S'

print(p)
print('\n')

if p == 'R' and u == 'S':
    print('the computer has won')
elif p == 'P' and u == 'R':
    print('the computer has won')
elif p == 'S' and u == 'P':
    print('the computer has won')
elif p == 'R' and u == 'P':
    print('You have won')
elif p == 'P' and u == 'S':
    print('You have won')
elif p == 'S' and u == 'R':
    print('You have won')
else:
    print('It is a draw')

a = []
b = []
c = []
d = []
for i in range(1,101):
    a = a + [i]
for i in range(1,101):
    b = b + [i*i]

for i in range(0,100):
    c = c + [int(a[i]) + int(b[i])]


for i in range(0,100,3):
    a[i] = 0

for i in range(0,100):
    d = d + [a[99-i]]


print(d)

f = open('Marks.txt','r')
a = f.readlines()
f.close()
e = open('Groups.txt','r')
b = e.readlines()
e.close()
marks = []
groups = []
names = []
g = open('Names.txt','r')
c = g.readlines()
g.close()
# convert into int
for item in a:
    marks = marks + [int(item)]

for item in c:
    names = names + [item.rstrip()]

for item in b:
    groups = groups + [item.rstrip()]

length = len(marks)
times = []
for i in range(0,length):
    t = 0
    for m in range(0,length):
        if marks[m] == marks[i]:
            t = t+1
    times = times + [t]


excel = []
for i in range(0,length):
    excel = excel + [(marks[i],times[i],names[i])]
print(excel)


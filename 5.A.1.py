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
excel = []
for i in range(0,length):
    excel = excel + [(names[i],groups[i],marks[i])]

for i in range(0,length):
    rang = range(i+1,length)
    for m in rang:
        if excel[m][2] < excel[i][2]:
            (excel[m],excel[i]) = (excel[i],excel[m])

print(excel)
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


excel = []
for i in range(0,len(marks)):
    excel = excel + [(names[i],groups[i],marks[i])]
print(excel)
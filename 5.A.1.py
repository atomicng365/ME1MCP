f = open('Marks.txt','r')
a = f.readlines()
f.close()
an = []
# convert into int
for item in a:
    an = an + [int(item)]
print(an)

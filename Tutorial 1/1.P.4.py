r1=[]
h1=[]
V1=[]
A1=[]
PI = 3.141592654
def Vol(h,r):
    V = PI*(h-2*r)*r**2 + PI*r**3*4/3
    return V
def SA(h,r):

    A = PI*(h-2*r)*r*2 + 4*PI*r**2
    return A

r = 0.1
h = 2*r
while Vol(h,r)<0.85:
    r = r+ 0.01
    h = 2*r
    while Vol(h,r)<0.85:
        h = h+0.01
    r1.append(r)
    h1.append(h)
    V1.append(Vol(h,r))
    A1.append(SA(h,r))
    h = 2*r  
min_area = min(A1)
min_area_index = A1.index(min_area)
print("min_area_index= ",min_area_index)
print("surface area = ",min_area)
print("Volume",V1[min_area_index])
print("height = ",h1[min_area_index])
print("radius = ",r1[min_area_index])
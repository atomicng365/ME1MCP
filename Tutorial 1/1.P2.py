import math
V = 0.85

PI = 3.141592654
def Rad(V,r):
    h = V/(PI*r**2)
    return h
def SA(V,r):
    h = V/(PI*r**2)
    A = 2*PI*r*h + 2*PI*r**2
    return A
r = 0.1
while r<= 1.5:
    print("r=",r,"m, h=",Rad(0.85,r),"m, surface=",SA(0.85,r),"mˆ2")
    r = r+ 0.05
print("r=",r,"m, h=",Rad(0.85,1.5),"m, surface=",SA(0.85,1.5),"mˆ2")
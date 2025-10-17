

PI = 3.141592654
def Vol(h,r):
    V = PI*(h-2*r)*r**2 + PI*r**3*4/3
    return V
def SA(h,r):

    A = PI*(h-2*r)*r*2 + 4*PI*r**2
    return A

r = 0.1
h = 2*r
while Vol(h,r)<0.9:
    r = r+ 0.05
    h = 2*r
    while Vol(h,r)<0.9:
        h = h+0.05
    print("r=",r,"m, h=",h,"m, Volume=",Vol(h,r),"mˆ3, surface=",SA(h,r),"mˆ2")
    h = 2*r  

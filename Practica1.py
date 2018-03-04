#Exercise 1

def squares(l):
    l2=[]

    for a in l:
        l2.append(a**2)

    return l2

print (squares([2,-1.2,3e2,1j]))
print (squares(i for i in range(10)))

def squares2(l):
    return [i**2 for i in l]

squares2(range(10))


#Exercise 2

def divisors(n):
    return [j for j in range(1,n) if n%j==0]

def is_perfect(n):
    return sum(divisors(n))==n

def write_perfect(m,n):
    for i in range(m,n+1):
        if is_perfect(i):
            print ("El numero",i,"es perfecto y sus divisores son",divisors)

write_perfect(1,1000)


#Exercise 3

d={'a':5,'b':10,'c':12,'d':11,'e':15,'f':20,'g':15,'h':9,'i':7,'j':2}
def hh(d):
    for x,y in d.items():
        print("{}: {}".format(x,"*"*y))

def hH(d):
    for x in d.keys():
        print("{0}: ".format(x),"*"*d[x])

hh(d)
hH(d)
print(sorted(d.values()))
print(max(d.values()))

def hV(d):
    m=max(d.values())
    cs=d.keys()
    for x in range(m,-1,-1):
        l=''
        for c in cs:
            if d[c]<x:
                l+=''
            else:
                l+='*'
            l+=' '
        print(l)
    print(' '.join(cs))

hV(d)


#Exercise 4

def depth(L):
    if isinstance(L,list):
        return 1 + max(depth(item) for item in L)
    else:
        return 0

print(depth(3))
print(depth([7,5,9,5,6]))
print(depth([1,[1,[1,[1,1],1],[1,1]],1]))


#Exercise 5

import math
class Projectile:
    def __init__(self,distance,height,vSpeed,hSpeed):
        self.distance=distance
        self.height=height
        self.vSpeed=vSpeed
        self.hSpeed=hSpeed

    def get_pos_x(self):
        return self.distance
    
    def get_pos_y(self):
        return self.height
    
    def refresh_position(self,t):
        currentvSpeed=self.vSpeed
        self.distance=currentvSpeed*t
        self.vSpeed-=9.8*t
        self.height+=((self.vSpeed+currentvSpeed)/2)*t
        

def land(height,speed,angle,interval):
    projectile=Projectile(0,height,speed*math.sin(math.radians(angle)),speed*math.cos(math.radians(angle)))
    nIntervals=0
    maxHeight=height

    while projectile.get_pos_y()>0:
        print("Projectile at ({},{})".format(abs(projectile.get_pos_x()),projectile.get_pos_y()))
        projectile.refresh_position(interval)
        nIntervals+=1
        if(projectile.get_pos_y()>maxHeight):
            maxHeight=projectile.get_pos_y()

    print("After {} intervals of {} seconds ({} seconds) the projectile has landed".format(nIntervals,interval,nIntervals*interval))
    print("It moved",abs(projectile.get_pos_x()),"metres")
    print("Maximum height achieved",maxHeight,"metres")

land(30,1,20,0.1)




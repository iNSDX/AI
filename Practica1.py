#Ejercicio 1
def cuadrados(l):
    l2=[]

    for a in l:
        l2.append(a**2)

    return l2

print (cuadrados([2,-1.2,3e2,1j]))
print (cuadrados(i for i in range(10)))

def cuadrados2(l):
    return [i**2 for i in l]

cuadrados2(range(10))


#Ejercicio 2
def divisores(n):
    return [j for j in range(1,n) if n%j==0]
def es_perfecto(n):
    return sum(divisores(n))==n
def escribe_perfectos(m,n):
    for i in range(m,n+1):
        if es_perfecto(i):
            print ("El numero",i,"es perfecto y sus divisores son",divisores)

escribe_perfectos(1,1000)


#Ejercicio 3
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


#Ejercicio 4

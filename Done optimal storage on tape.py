x=[2,67,5,43,8,91,83,57]
y=3
def tapeoptimization(x,y):
    t=[]
    for i in range(len(x)):
        t.append([x[i],i])
    t.sort()
    z=[]
    for i in range(len(t)):
        z.append(((t[i][1])%y)+1)
    return z
print(x)
print(sorted(x))
print(tapeoptimization(x,y))
def parent(u):
    while m[u]!=-1:
        u=m[u]
    return u        

V=3
edges=[[0, 1, 5], [1, 2, 3], [0, 2, 1]]
m=[-1]*V
E=[]
for x,y,z in edges:
    E.append([z,x,y])
E.sort()
sum=0
def main():
            global sum
            for w,u,v in E:
                if parent(u)!=parent(v):
                    sum=sum+w
                    m[parent(u)]=parent(v)
            return sum
print(main())
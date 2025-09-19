w=[14,18,4,5,19]
p=[2,10,20,8,9]
m=25
def knapsack(w,p,m):
    x=[]
    for i in range(len(w)):
        x.append([p[i]/w[i],i])
    x.sort()
    t=[0]*len(x)
    i=len(x)-1
    while i>-1:
        if m<w[x[i][1]]:
            break
        t[x[i][1]]=1
        m=m-w[x[i][1]]
        i=i-1
    if i>=0: #this line (don't forget) notes me sort hi descending order me kiya hai to i<len(w) hai
        t[x[i][1]]=m/w[x[i][1]]
    return t
print(knapsack(w,p,m))


x=[]
deadline = [2, 1, 2, 1, 1]
profit = [100, 19, 27, 25, 15]
for _ in range(len(profit)):
    x.append([profit[_],deadline[_]])
x.sort(reverse=True)
maxprofit=0
count=0
y=[0]*max(deadline)
for i in range(len(x)):
    t=x[i][1]-1
    while t>-1 and y[t]!=0:
        t=t-1
    if t>-1:
        y[t]=1
        maxprofit=maxprofit+x[i][0]
        count=count+1
print( y,[count,maxprofit])
import time
import random
from matplotlib import pyplot as plt
def avgPrefix1(x):
    A=[]
    for i in range(len(x)):
        sum=0
        for j in range(i+1):
            sum=sum+x[j]
        Average=sum/(i+1)
        A.append(Average)
    return A
def avgPrefix2(x):
    sum=0
    A=[]
    for i in range(len(x)):
        sum=sum+x[i]
        Average=sum/(i+1)
        A.append(Average)
    return A
print(avgPrefix1([2,1,5,6,8,3]))
print(avgPrefix2([2,1,5,6,8,3]))



array=[]
for k in range(1000):
    t=[]
    for l in range(k):
        t.append(random.randint(0, 1000))
    array.append(t)
x=[]
y=[]
for i in range(1000):
    start=time.perf_counter()
    for m in range(5):
        avgPrefix1(array[i])
    end=time.perf_counter()
    x.append((end-start)/5)


    start=time.perf_counter()
    for m in range(5):
        avgPrefix2(array[i])
    end=time.perf_counter()
    y.append((end-start)/5)
z=[]
for j in range(1000):
    z.append(j)
plt.plot(z,x)
plt.show()
plt.plot(z,y)
plt.show()
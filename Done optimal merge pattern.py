import heapq
x=[2 ,3 ,4 ,5 ,6 ,7]
heap=x
sum=0
def func():
    global sum
    while len(heap)>1:
        x1=heapq.heappop(heap)
        x2=heapq.heappop(heap)
        y=x1+x2
        sum=sum+y
        heapq.heappush(heap,y)
    return sum
print(func())
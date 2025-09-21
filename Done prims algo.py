import heapq

def prims(heap):
    while heap:
        global sumvar
        w,node=heapq.heappop(heap)
        if visited[node]:
                    continue 
        visited[node]=True
        sumvar=sumvar+w
        for key,value in dictionary[node].items():
                    if visited[key]!=True:
                        heapq.heappush(heap,[value,key])
    return sumvar 
sumvar=0
V=3
edges=[[0, 1, 5], [1, 2, 3], [0, 2, 1]]  
dictionary={v:{} for v in range(V)}
for x,y,z in edges:
        dictionary[x][y]=z
        dictionary[y][x]=z
        
heap=[[0,0]]
visited=[False]*V                
print(prims(heap))
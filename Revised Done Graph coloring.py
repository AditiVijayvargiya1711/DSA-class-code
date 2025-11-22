def graphColoring(v, edges, m):
        # code here
        dictionary={i:[] for i in range(v)}
        for u, w in edges:
            dictionary[u].append(w)
            dictionary[w].append(u)
            
        y=[-1]*v
        def possible(x,i):
            for j in dictionary[x] :
                if i==y[j]:
                    return False
            return True
                
        def main(x):
            if v==x:
                return True
            for i in range(m):
                if possible(x,i):
                    y[x]=i
                    if main(x+1)==True:
                        return True
                    y[x]=-1
            return False
            
        return main(0)
print(graphColoring(v= 4, edges = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]], m = 3))
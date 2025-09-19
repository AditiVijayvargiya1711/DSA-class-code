x=[2,89,7,65,43,76,1,90]
def quicksort(i,j):
        if i>=j: #i==j will not work
             return
        pivot=x[j-1]
        m=i   #m=i not 0
        for k in range(i,j-1):
            if x[k]<=pivot:
                x[m],x[k]=x[k],x[m]
                m=m+1
        x[m],x[j-1]=x[j-1],x[m]
        quicksort(i,m)
        quicksort(m+1,j)
        return x
print(quicksort(0,len(x)))

'''time complexity=n^2'''
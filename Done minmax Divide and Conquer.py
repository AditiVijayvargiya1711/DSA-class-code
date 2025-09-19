
def maxmin(A):
    min=A[0]
    max=A[0]
    for i in range(1,len(A)):
        if A[i]>max:
            max=A[i]
        elif A[i]<min:
            min=A[i]
    return max,min
print(maxmin([2,9,7,6,5,8,4,3,1,0]))

A=[2,3,5,7,4,1,9,8]
def maxminrec(i,j):
    if i==j:
        return A[i],A[i]
    if i==j-1:
        return max(A[i],A[j]), min(A[i],A[j])
    mid=i+(j-i)//2
    lmax,lmin=maxminrec(i,mid)
    rmax,rmin=maxminrec(mid,j)
    return max(lmax,rmax), min(lmin,rmin)

print(maxminrec(0,len(A)-1))
    

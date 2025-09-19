def mergesort(arr,low,high):
    mid=low+(high-low)//2
    if mid==high:
        return arr[mid]
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    return merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    left=[]
    right=[]
    for i in range(low,mid+1):
        left.append(arr[i])
    for j in range(mid+1,high+1):
        right.append(arr[j])
    left.append(float('inf'))
    right.append(float('inf'))
    k=low
    i=0
    j=0
    while k<high+1:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1

    return arr
def mergesort2(low,high):
    mid=low+(high-low)//2
    if mid==high:
        return [arr2[mid]]
    left=mergesort2(low,mid)
    right=mergesort2(mid+1,high)
    return merge2(left,right)

def merge2(a,b):
    i=0
    j=0
    x=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            x.append(a[i])
            i=i+1
        else:
            x.append(b[j])
            j=j+1
    while i<len(a):
        x.append(a[i])
        i=i+1
    while j<len(b):
        x.append(b[j])
        j=j+1
    return x

arr=[246,31,70,9,58,20]
arr2=[246,31,70,9,58,20]
print(mergesort(arr,0,len(arr)-1))
print(mergesort2(0,len(arr)-1))

'''
[1,5,4,3] mid=index 1
[2,6,9,4,1] mid=index 2


Time Complexity=n(logn)
'''

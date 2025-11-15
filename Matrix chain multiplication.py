arr = [2, 1, 3, 4]
def main1(i,j):
    if i==j:
        return 0
    ans=float('inf')
    for k in range(i,j):
        x=main1(i,k)+main1(k+1,j)+arr[i-1]*arr[j]*arr[k]
        ans=min(x,ans)
    return ans
dp2=[[float('inf')]*len(arr) for i in range(len(arr))]
def main2(i,j):
    if i==j:
        return 0
    if dp2[i][j]!=float('inf'):
        return dp2[i][j]
    for k in range(i,j):
        x=main2(i,k)+main2(k+1,j)+arr[i-1]*arr[j]*arr[k]
        dp2[i][j]=min(x,dp2[i][j])
    return dp2[i][j]
def main3() :  
    dp=[[float('inf')]*(len(arr)) for i in range(len(arr)-1)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                dp[i-1][j]=0
    for i in range(len(arr)-1,0,-1):
        for j in range(i,len(arr)):
            for k in range(i,j):
                x=dp[i-1][k]+dp[k][j]+arr[i-1]*arr[j]*arr[k]
                dp[i-1][j]=min(x,dp[i-1][j])
    return dp[0][len(arr)-1]

        
print(main1(1,len(arr)-1),main2(1,len(arr)-1), main3())
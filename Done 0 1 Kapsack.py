W = 4
val= [1, 2, 3]
wt= [4, 5, 1]
#recursion
def main1(i,W):
            if i==len(val):
                return 0
            if W<=0:
                return 0
            take=0
            if wt[i]<=W:
                take=val[i]+ main1(i+1,W-wt[i])
            nottake=main1(i+1,W)
            return max(take,nottake)

#recursion with dp
dp=[[-1]*(W+1) for i in range(len(val))]
def main2(i,W):
            if i==len(val):
                return 0
            if W<=0:
                return 0
            if dp[i][W]!=-1:
                return dp[i][W]
            take=0
            if wt[i]<=W:
                take=val[i]+ main2(i+1,W-wt[i])
            nottake=main2(i+1,W)
            dp[i][W]=max(take,nottake)
            return max(take,nottake)
#tabulation
def main3():
    dp=[[0]*(W+1) for i in range(len(val)+1)]
    for i in range(len(val)-1,-1,-1):
            for j in range(0,W+1):
                take=0
                if wt[i]<=j:
                    take=val[i]+ dp[i+1][j-wt[i]]
                nottake=dp[i+1][j]
                dp[i][j]=max(take,nottake)
    return dp[0][W]
#tabulation with space optimization
def main4():
    curr=[0]*(W+1)
    prev=[0]*(W+1)
    for i in range(len(val)-1,-1,-1):
            for j in range(0,W+1):
                take=0
                if wt[i]<=j:
                    take=val[i]+ prev[j-wt[i]]
                nottake=prev[j]
                curr[j]=max(take,nottake)
            prev=curr[:]
    return curr[W]
    
print(main1(0,W),main2(0,W),main3(),main4())
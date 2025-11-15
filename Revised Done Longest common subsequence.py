text1="abcde"
text2 = "acde" 
def main1(i,j):
    if i==len(text1) or j==len(text2):
        return 0
    take=0
    if text1[i]==text2[j]:
        take=1+main1(i+1,j+1)
    nottake=max(main1(i+1,j),main1(i,j+1))
    return max(take,nottake)

dp2=[[-1]*len(text2) for _ in range(len(text1))]
def main2(i,j):
    if i==len(text1) or j==len(text2):
        return 0
    if dp2[i][j]!=-1:
        return dp2[i][j]
    take=0
    if text1[i]==text2[j]:
        take=1+main2(i+1,j+1)
    nottake=max(main2(i+1,j),main2(i,j+1))
    dp2[i][j]=max(take,nottake)
    return max(take,nottake)

def main3():
    dp3=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            take=0
            if text1[i]==text2[j]:
                take=1+dp3[i+1][j+1]
            nottake=max(dp3[i+1][j],dp3[i][j+1])
            dp3[i][j]=max(take,nottake)
    return dp3[0][0]


def main4():
    prev=[0]*(len(text2)+1)
    curr=[0]*(len(text2)+1)
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            take=0
            if text1[i]==text2[j]:
                take=1+prev[j+1]
            nottake=max(prev[j],curr[j+1])
            curr[j]=max(take,nottake)
        prev=curr[:]
    return curr[0]
print(main1(0,0), main2(0,0),main3(),main4())
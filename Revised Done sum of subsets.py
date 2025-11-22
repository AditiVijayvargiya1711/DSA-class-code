def main1(i,summation):
        if summation==sum:
            return True
        if i==len(arr):
            return False
        take=main1(i+1, summation+arr[i])
        nottake=main1(i+1,summation)
        return nottake or take
def main2(i,summation):
            if summation==sum:
                return True
            if summation>sum:
                return False
            if i==len(arr):
                return False
            if dp2[i][summation]!=None:
                return dp2[i][summation]
            take=main2(i+1, summation+arr[i])
            nottake=main2(i+1,summation)
            dp2[i][summation]=nottake or take
            return nottake or take
def main3():
        dp3=[[False]*(sum+1) for i in range(len(arr)+1)]
        for _ in range(len(arr)+1):
            dp3[_][sum]=True
        for i in range(len(arr)-1,-1,-1):
            for summation in range(sum,-1,-1):
                take=False
                if summation+arr[i]<=sum:
                    take=dp3[i+1][ summation+arr[i]]
                nottake=dp3[i+1][summation]
                dp3[i][summation]=nottake or take
            
        return dp3[0][0]
        
def main4():
    prev=[False]*(sum+1)
    prev[sum]=True
    curr=[False]*(sum+1)
    for i in range(len(arr)-1,-1,-1):
        curr[sum]=True
        for summation in range(sum,-1,-1):
            take=False
            if summation+arr[i]<=sum:
                take=prev[ summation+arr[i]]
            nottake=prev[summation]
            curr[summation]=nottake or take
        prev=curr[:]
    return curr[0]



arr=[3, 34, 4, 12, 5, 2]
sum=9
dp2=[[None]*sum for i in range(len(arr))]
print(main1(0,0),main2(0,0),main3(),main4())
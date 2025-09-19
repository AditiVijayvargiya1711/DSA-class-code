nums=[3,7,2,2,4,6,4,5,9]


for i in range(len(nums)-1):
    x=i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[x]:
            x=j
    nums[i],nums[x]=nums[x],nums[i]
print(nums)


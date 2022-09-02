def brute_force(nums,target):
    for i in range(len(nums)): #O(N)
        for j in range(i+1,len(nums)):
            if target==nums[i]+nums[j]: #O(N*N)
                print(i,j)
                return

def optimal_approach(nums,target):
    dic={}
    for i in range(len(nums)):   #O(N)
        complement=target-nums[i]
        if complement in dic:
            print(i,dic[complement])
            return
        dic[nums[i]]=i



if __name__ == '__main__':
    nums=[1,4,13,3,2,6,4,2,1]
    target = 3
    brute_force(nums,target)
    optimal_approach(nums,target)











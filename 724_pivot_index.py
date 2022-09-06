if __name__ == '__main__':
    nums=[2,-1,1]

    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
    ls=0
    rs=sum
    for i in range(len(nums)):
        rs=rs-nums[i]
        if ls==rs:
            print(i)
            exit()
        ls=ls+nums[i]
    print(-1)
















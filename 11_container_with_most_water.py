def brute_force(height):
    area=0
    for i in range(len(height)): #N
        x=1
        for j in range(i+1,len(height)):
            temp = x * min(height[i],height[j])
            if temp>area:
                area=temp
            x+=1 #O(N*N)
    print(area)


def optimal_approach(height):
    area=0
    x=len(height)-1
    l=0
    r=len(height)-1

    while l!=r: #O(N)
        temp = x* min(height[l],height[r])
        if temp>area:
            area=temp
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
        x-=1
    print(area)


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    brute_force(height)
    optimal_approach(height)


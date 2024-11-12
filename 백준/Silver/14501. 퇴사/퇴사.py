n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int,input().split())))

ans = 0

def check(now, money):
    global ans
    #print(now, money)

    
    if(ans < money):
        ans = money

    for i in range(now, n):
        if(i + nums[i][0] <= n):
            check(i + nums[i][0], money + nums[i][1])



check(0, 0)


print(ans)

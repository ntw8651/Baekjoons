def isPel(a):
    a = str(a)
    for i in range(len(a)//2+1):
        if(a[i] != a[-(i+1)]):
            return 0
    else:
        return 1


nums = [0 for i in range(0, 1001)]
for i in range(1, 1000):
    if(i*i > 1001):
        break
    else:
        if(isPel(i*i) and isPel(i)):
            nums[i*i] = 1
            
t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    count = 0
    for i in range(a, b+1):
        if(nums[i]):
            count+=1
    print("Case #"+str(_+1)+":", count)

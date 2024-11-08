# 그냥 하는거에다가 2진탐색정도 넣는거네
n, m = map(int, input().split())
nums = [0] + list(map(int,input().split()))
sums = [0] + [0 for i in range(n)]
sumN = 0
for i in range(1, n+1):
    sumN += nums[i]
    sums[i] = sumN

left = 0
right = n

def find(size, arr):
    result = 0
    for i in range(n-size+1):
        if(result < arr[i+size] - arr[i]):
            result = arr[i+size] - arr[i]
    return result

flag = 1
while(left <= right):
    mid = (left + right)// 2
    if(mid>n):
        flag = 0
        break
    result = find(mid, sums)
    if(result == m):
        flag = 1
        break
    elif(result < m):
        left = mid + 1
    else:
        right = mid - 1

if(flag == 0):
    print(0)
else:
    if(result < m):
        if(mid == n):
            print(0)
        else:
            print(mid+1)
    else:
        print(mid)




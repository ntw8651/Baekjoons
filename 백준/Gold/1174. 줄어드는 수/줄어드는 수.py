'''
9876543210
'''
nums = [i for i in range(10)]
left = 0
right = 10
count = 10
flag = 1
while(flag):
    flag = 0
    for j in range(left, right):
        for k in range(9, -1, -1):
            if(nums[j] % 10 > k):
                nums.append(nums[j]*10+k)
                count+=1
                flag = 1
    left = right
    right = count
    
n = int(input())        
nums.sort()
if(n > count):
    print(-1)
else:
    print(nums[n-1])

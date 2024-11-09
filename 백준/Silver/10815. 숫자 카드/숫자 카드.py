n = int(input())
nums = set()
for i in list(map(int,input().split())):
    nums.add(i)
n = int(input())
for i in list(map(int,input().split())):
    if(i in nums):
        print(1, end = " ")
    else:
        print(0, end = " ")

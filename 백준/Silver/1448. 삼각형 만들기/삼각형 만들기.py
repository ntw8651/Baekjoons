import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

flag = -1
arr.sort()
for i in range(n-2):
    if(max(arr[i:i+3]) < sum(arr[i:i+3]) - max(arr[i:i+3])):
        flag = arr[i] + arr[i+1] + arr[i+2]

print(flag)

from collections import deque
#대충 deque로 돌아가면서 추가 or 넣 을 반복하면 될 듯
n, k = map(int,input().split())
count = k
ans = '<'
nums = deque([str(i+1) for i in range(n)])

for i in range(n):
    for j in range(k-1):
        nums.append(nums.popleft())
    ans += nums.popleft() + ', '

print(ans[:-2] + '>')

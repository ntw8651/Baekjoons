n = int(input())
types = list(map(int, input().split()))
qustack = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
'''
스택이면 그대로
큐면 바꾸기

어..어차피 스택은 안건드리고
큐면 진짜 큐처럼 동작하니까
그냥 큐인 애들만 모아서 진짜 큐를 만들면 되겠구나
'''
queue = []
for i in range(n-1, -1, -1):
    if(types[i] == 0):
        queue.append(qustack[i])

#그냥 뒤집고 append해가면서 앞부터 출력 고


for i in range(m):
    queue.append(nums[i])
    print(queue[i], end = " ")
    

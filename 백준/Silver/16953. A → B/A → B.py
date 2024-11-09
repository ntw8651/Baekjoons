from collections import deque as dq
a, b = map(int, input().split())
#최소값이니까 bfs구만
#연산은 두개
#* 2
#*10 + 1
que = dq([])
que.append([a, 1])
flag = 0
while(que):
    value, count = que.popleft()
    #print(value, count)
    if(value == b):
        flag = 1
        print(count)
        break
    elif(value < b):
        que.append([value*2, count+1])
        que.append([value*10+1, count+1])
    
if(not flag):
    print(-1)

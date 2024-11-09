#컨베이어 벨트 위의 로봇
from collections import deque as dq

n, k  = map(int, input().split())
convey = dq(list(map(int, input().split())))
convey_r = dq([0 for i in range(n)])
count = 0 
while(k>0):
    count+=1
    
    #1
    convey.appendleft(convey.pop())
    convey_r.appendleft(convey_r.pop())
    

    #2
    if(convey_r[n-1] == 1):
        #convey[n-1] -= 1
        convey_r[n-1] = 0
        #if(convey[n-1] == 0):
        #    k -= 1
        
    for i in range(n-2, -1, -1):
        if(convey_r[i] == 1 and convey[i+1] > 0 and convey_r[i+1] == 0):
            convey_r[i+1] = 1
            convey_r[i] = 0
            convey[i+1] -= 1
            if(convey[i+1] == 0):
                k-=1

    if(convey_r[n-1] == 1):
        #convey[n-1] -= 1
        convey_r[n-1] = 0
        #if(convey[n-1] == 0):
        #    k-=1

    #3
    if(convey[0] > 0):
        convey[0] -= 1
        convey_r[0] = 1
        if(convey[0] == 0):
                k-=1

    
    if(convey_r[n-1] == 1):
        #convey[n-1] -= 1
        convey_r[n-1] = 0
        #if(convey[n-1] == 0):
        #    k-=1

    
    
print(count)


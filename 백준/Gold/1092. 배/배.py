n = int(input())
crain = list(map(int,input().split()))
lastPos = [0 for i in range(n)]
m = int(input())
box = list(map(int,input().split()))
t = 0
box.sort(reverse = True)
if(max(crain) < max(box)):
    print(-1)
else:
    flag = 1
    while(flag):
        flag = 0
        t+=1
        for i in range(n):
            for j in range(lastPos[i], m):
                if(box[j] != -1):
                    if(box[j] <= crain[i]):
                        box[j] = -1
                        flag = 1
                        break
                lastPos[i] = j
            
    print(t-1)

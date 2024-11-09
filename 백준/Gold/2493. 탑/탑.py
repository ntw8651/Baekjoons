
N = int(input())
tops = list(map(int, input().split()))

signals = [] #stack

endder = [0 for i in range(N)]
counter = 1
subCounter = 0

for i in range(N-2, -1, -1):
    signals.append(i+1)
    for p in range(len(signals)):
        if(tops[signals[-1]] < tops[i]):
            endder[signals[-1]] = i + 1
            counter+=1
            
            del signals[-1]
        else:
            break
        
print(' '.join(map(str, endder)))

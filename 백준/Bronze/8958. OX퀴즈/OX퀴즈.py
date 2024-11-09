import sys
T = int(sys.stdin.readline())

for i in range(T):
    score = int(0)
    combo = int(0)
    result = str(sys.stdin.readline())
    for p in result:
        if p == 'O':
            combo+=1
            score += combo
        else:
            combo = 0
    
    print(score)
            
            

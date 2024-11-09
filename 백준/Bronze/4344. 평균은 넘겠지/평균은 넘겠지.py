import sys
C = int(sys.stdin.readline())

for i in range(C):
    
    people = list(map(int, sys.stdin.readline().split()))
    people_len = people[0]
    del people[0]
    you_good = 0
    punggyen = sum(people)/people_len
    
    for p in people:
        if(p > punggyen):
            you_good +=1
    print('%0.3f' % float(you_good/people_len*100)+'%')
        
        
            
            
#솔직히 나정도면 평균은..

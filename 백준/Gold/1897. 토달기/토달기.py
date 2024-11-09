'''

내가 생각하는 방식은...
1. 각 영문자가 등장하는 횟수를 정리한다 <- 생각해보니까 순서가 필요하네ㅎ;;
-> 그냥... 저장
2. 총 글자 수로 정렬한다
3. 글자 비교
4. 한칸 위에 있는 걸로 만들 수 있는 모든 글자는 승진한다
5. 승진한 글자를 갖고, 4번을 반복한다
6. 더이상 승진할 수 있는 글자가 없으면 직전의 것을 출력한다

근데 뭔가 시간초과의 향기가 폴폴나는데

습...이러면...괜찮지 않을까?
안이;;뭐지

ㅎ.ㅎ....이번...에야말로..!
'''
import sys
input = sys.stdin.readline

n, word = input().split()
n = int(n)
alls = [[] for i in range(82)]#글자수 따라서
for i in range(n):
    inp = input().rstrip()
    alls[len(inp)].append([0, inp])

#생각해보면 글자수는 다시 저장할 필요가 없음.
#아..ㅋㅋㅋ 0에서 1로 바꿔야지 생각해보니까


alls[3] = [[1, word]]#그리고 배열을 다시저장하지 말고, 대신 ok인지 no인지 bool을 저장해주자
now = 3
while(True):
    now+=1
    find = 0
    for i in alls[now-1]:
        if(not i[0]):
            continue
        
        checks = set()
        length = len(alls[now])
        for nw in range(length):
            flag = 0
            
            if(alls[now][nw][1] in checks):
                continue
            j=0
            while(j < now-1):
                if(i[1][j] != alls[now][nw][1][j+flag]):
                    #print(j, flag, i, alls[now][nw])
                    flag += 1
                    j-=1
                if(flag > 1):
                    flag = -1
                    break
                j+=1

                
            if(flag == 0):
                flag = 1
                
            if(flag == 1 or flag == 0):#아 근데 똑같은게 여러개 뜨면 어떠카지 set에다 묶어놓자
                checks.add(alls[now][nw][1])
                find = 1
                alls[now][nw][0] = 1
                
                
    if(find == 0):
        length = len(alls[now-1])
        for i in range(length):
            if(alls[now-1][i][0]):
                print(alls[now-1][i][1])
                flag = -9999
                break
        if(flag==-9999):
            break


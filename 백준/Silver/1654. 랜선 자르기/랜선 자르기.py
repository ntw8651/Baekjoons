import sys
input = sys.stdin.readline
K, N = map(int,input().split())

lines = []
la= lines.append

for i in range(K):
    num = int(input())
    la(num)

def Check(length):
    count = 0
    for i in lines:
        count+=i//length
        if(count>=N):
            return True
        
    return False
#아 대충 미드 왼쪽 오른쪽 셋 중 하나겠지ㅋㅋ라는 마인드로 해버리면 되는구나?


#mid어쩌고에서 잘못되었따 이말이지
#아 그러네  mid를 포함 안해도 되는구나 생각해보니까
llength = 0
rlength = sum(lines)//N +1
while(llength <= rlength):
    mid =(llength+rlength)//2    
    if(Check(mid)):
        llength = mid + 1
    else:
        rlength = mid - 1
    
#뭔가 이거랑 비슷하게 마인크래프트를 시도하다가 다른 방법이 먹혔던 것 같은데...
# True : N개 충족
# False : N개 미충족
if(Check(mid+1)):
    print(mid+1)
elif(Check(mid)):
    print(mid)
else:
    print(mid-1)
    #아ㅋㅋㅋㅋㅋㅋㅋㅋㅋ잠깐ㅋㅋㅋㅋㅋㅋㅋprint안빼고 넣었잖아ㅋㅋㅋㅋㅋㅋ
    #ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#print(length)

##...2진...탐색...해볼까?

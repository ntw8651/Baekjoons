num = int(input())
arr = list(map(int, input().split()))

#증가+감소 횟수 즉 꺾이는 횟수
maxPoint = 0

change = True
#아 단증으로 시작하도록 안 맞혀줬구나
#단증시작, 단증감소끝 을 맞춰야겠구나?

lastNum = -1
arr.insert(0, -1)

for i in arr:
    if(change and lastNum>i):
        
        maxPoint+=1
        change = False
        
    if(change == False and lastNum<i):
        change = True
    lastNum = i
    
#극대점구하기 까지는 같네?

#아 그리고 여기서 단증으로 시작하냐 단감으로 시작하냐에 따라 극대값 수도 달라지는구
#가 아니라 저기서 앞에 없어도 저거로 봤는데 어... 어?
#음.... 뭐지?
#과거찬스
count = 0
if(change and maxPoint!=0):#그치 0이 아니여야 하는거잖아 maxPoint 즉 최고값 그게 없다면 이미 정렬이니
    maxPoint+=1
#7이 4가 되었네
#그렇다면 횟수구하기를 만들면
#여기서 극대점이 3
#아 그리고 저렇게 극대점은 3개 3개로 같은데 교체 횟수는 다르잖 왜 같아보이지 버근가
    #다시 보면서 이

while(maxPoint):
    if(maxPoint%2!=0 and maxPoint!=1):#아하 이 점선은 여기서 하는게아니지
        #이거는 극대가 홀수인거고 단감 마무리는 밖에서 해야지 그래 그런거였어
        #잠깐 그
        maxPoint+=1
    maxPoint = int(maxPoint/2)
    
    count+=1

print(count)
#3번이 맞다 누가 맞대 이넘아

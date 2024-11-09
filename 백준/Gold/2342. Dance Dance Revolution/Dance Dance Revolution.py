'''
보존 우선 순위
만약 다음 턴에 밟아야 하는 애를 이미 밟고 있다면 우선순위1
이번 발자국 까지 가는 데 2밖에 안쓴다면 우선순위2
그리고 3이 우선순위3

왠만하면 0의 발판은 늦게 시작하는 게 좋긴 할 듯 함
왜냐면 연속발판에 걸렸는데 다른 발이 4쓰고 넘어가야할 수 있으니
근데 또 만약 마지막 발이라면 연속 밟기가 아닌 이상
중앙 발을 꺼내는 게 이득인 듯

음음 예측했다고
'''
#만약 중앙에 발 없으면 무조건 +3
        #그냥 "가만히"를 할 수 있으면 무조건 이득인가?
        #그치 무조건 "가만히" 를 하면 2턴에서 최대 1+4가 나와서 3+3보단 작지
        #근데 가만히의 타이밍인거지, 지금 가만히와 나중 가만히.
        #만약 지금 가만히가 한 칸 뛰어 넘어야 하는 가만히면
        #차라리 나중에 가만히가 있다는 게 보장될 경우 그 가만히를 위해
        #이걸 버리고 그 가만히를 챙기는...
        #이거... 뭔가 이케가 아니라 우선순위큐 쓰는 문제인 것 같긴 해...
        #왜냐면 10만이잖아... nlogn을 저격한 n이란 말이지...
        #근데 문제점은 얘는 한 번당 2배로 늘어난단 점이야
        #왼발 움직이는 경우의 수와 오른발 움직이는 경우의 수
        #어? 근데 발 배치가 똑같아지는 때가 오면 거기서 최대인 애만 고르면
        #되네? 발 배치의 총 개수는 어차피 5C2밖에 없잖아 10개네 어? 그러네??
        #뜨 가자미~



'''
나니?
#지금 밟고 있는 판을 담은 우선순위 큐 하나

#현재로 귀결될 수 있는 모든 경우의 수를 담은 배열(총 4개겠네, 하나는 고정이니까, 그냥 5*5배열 만들자)


그냥 작은 수를 움직이거나 큰 수를 움직이는 두가지 경우만 따져주면 되는데...


일단 뭐 시간 초과는 안 났네
'''



n = list(map(int,input().split()))

length = len(n)
INF = 2**30
foots = [[0, n[0], 2]]#왼발, 오른발, 현재 answer

fp = foots.pop
fa = foots.append

def check(dest, now):
    if(now == 0):
        return 2
    if(dest == now):
        return 1
    elif(dest - now == 2 or dest - now == -2):
        return 4 #아ㅋㅋㅋ이게 4잖아;;
    else:
        return 3


for i in range(1, length-1):
    nums = [[INF for i in range(5)] for j in range(5)]
    while(foots != []):
        now = fp()
        if(nums[n[i]][now[1]] > now[2] + check(n[i], now[0])):#왼발
            #왼발 옮긴 게 기존보다 이득이다! 추가
            nums[n[i]][now[1]] = now[2] + check(n[i], now[0])
            nums[now[1]][n[i]] = now[2] + check(n[i], now[0])
            
        if(nums[now[0]][n[i]] > now[2] + check(n[i], now[1])):#오른발
            nums[now[0]][n[i]] = now[2] + check(n[i], now[1])
            nums[n[i]][now[0]] = now[2] + check(n[i], now[1])


    for y in range(5):
        for x in range(y, 5): #이제 INF아닌 애들 다시 foots에 넣어주기
            if(nums[y][x] != INF):
                fa([x,y,nums[y][x]])
    #아니 근데 어차피 풋스텝에 다시 채울꺼니까 2개가 필요한게 아니구나?
if(length == 1):
    print(0)
else:
    print(min(foots, key = lambda x : x[2])[2])

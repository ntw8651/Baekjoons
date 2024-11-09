#음하하 방금까지 뭐풀었더라  구래 이 줄세우기를 호다닥 풀어버리고 왔지 음하하
#아무튼 그래서 이제 갑자기 자신감 뿜뿜해서 구슬동자 풀러 옴
#아;; 녹화 더 빨리 킬껄
'''
왜 갑자기 이걸 하려고 하느냐?
1. 클래스 5에서 푼 사람 수로 정렬함
와 많이 풀었자나?
2. 그리고 문제 읽다보니 어? 잠만 뭔가 알 것 같은데?
오키? 고고혓~

아무튼 대략 생각 아니지 문제 볼 시간좀 드

아무튼 내가 딱 눈치 챈 게 하나 있지.
이건 10번 안에 들어가야 한단 거야.
근데 방향은 4개지. 이거 완전 전체탐색이자낭@!!!

'''
import sys
sys.setrecursionlimit(10**7)
n, m = map(int,input().split())
answer = 100
mapper = []
b = [0, 0]
r = [0, 0]
for i in range(n):
    mapper.append(list(input()))
    for k in range(m):
        #B랑 R위치 따놓기
        if(mapper[i][k] == 'R'):
            r = [k, i]
        elif(mapper[i][k] == 'B'):
            b = [k, i]
            
def find(rp, bp, mapper, count, direct):
    global answer
    #print(rp)
    #direct = 방향
    #0 위 1 오 2 밑 3 왼
    
    if(direct == 0):
        resultR = vertical(rp[0], rp[1], -1, mapper, bp)
        if(resultR != -1):
            rp[1] = resultR
        else:
            rp = [-1, -1]
            
        resultB = vertical(bp[0], bp[1], -1, mapper, rp)
        if(resultB != -1):
            bp[1] = resultB
            if(resultR != -1):
                resultR = vertical(rp[0], rp[1], -1, mapper, bp)
                if(resultR != -1):
                    rp[1] = resultR
    
    elif(direct == 1):
        resultR = horizontal(rp[0], rp[1], 1, mapper, bp)
        if(resultR != -1):
            rp[0] = resultR
        else:
            rp = [-1, -1]
            
        resultB = horizontal(bp[0], bp[1], 1, mapper, rp)
        if(resultB != -1):
            bp[0] = resultB

            if(resultR != -1):
                resultR = horizontal(rp[0], rp[1], 1, mapper, bp)
                if(resultR != -1):
                    rp[0] = resultR
        
    elif(direct == 2):
        resultR = vertical(rp[0], rp[1], 1, mapper, bp)
        if(resultR != -1):
            rp[1] = resultR
        else:
            rp = [-1, -1]
            
        resultB = vertical(bp[0], bp[1], 1, mapper, rp)
        if(resultB != -1):
            bp[1] = resultB
            if(resultR != -1):
                resultR = vertical(rp[0], rp[1], 1, mapper, bp)
                if(resultR != -1):
                    rp[1] = resultR
            
    elif(direct == 3):
        resultR = horizontal(rp[0], rp[1], -1, mapper, bp)
        if(resultR != -1):
            rp[0] = resultR
        else:
            rp = [-1, -1]
            
        resultB = horizontal(bp[0], bp[1], -1, mapper, rp)
        if(resultB != -1):
            bp[0] = resultB
            if(resultR != -1):
                resultR = horizontal(rp[0], rp[1], -1, mapper, bp)
                if(resultR != -1):
                    rp[0] = resultR
    #red위치
    #blue위치
    #count

    #같은 턴에 둘다 빠지면 실패
    if(resultR == -1 and resultB == -1):
        
        return 0
    elif(resultR == -1):
        #빨강만 빠지면 성공
        if(count < answer):
            answer = count
        return 0
    elif(resultB == -1):
        return 0
    else:
        if(count >= answer):
            return 0
        if(count < 10):
            #방금 했던 것의 반대 방향 빼고
            for i in range(4):
                if(i != direct):
                    find(rp.copy(), bp.copy(), mapper, count+1, i)
        else:
            return 0
        #둘다 안 빠졌고 아직 횟수 괜찮으면
#horizon vertical로 이동은 2번씩 시켜줘야겠네
def horizontal(x, y, v, mapper, another):#anox anoy는 r-b서로 반대꺼
    #v가 +면 오른쪽
    #-면 왼쪽
    #벽 직전 위치 찾기
    #해서 이동하면 가게 될 위치랑 거리 반환
    #만약 O를 찾게 되면 특별한 값 반환

    #그냥 정답이면 음수 거리로 반환해주고
    #벽에 닿으면 직전 양수 거리로 반환해주자 아니 거리말고 위치
    if(v<0):
        for i in range(x-1, -1, -1):
            if(mapper[y][i] == 'O'):#정답임니다!!
                return -1
            elif(mapper[y][i] == '#'):#직전값 반환
                return i+1
            elif(i == another[0] and y == another[1]):
                return i+1
    else:
        for i in range(x+1, m, 1):
            if(mapper[y][i] == 'O'):#정답임니다!!
                return -1
            elif(mapper[y][i] == '#'):#직전값 반환
                return i-1
            elif(i == another[0] and y == another[1]):
                return i-1
            
#뭔가 맨날 배열을 받는 순서대로 쭉 해서 하다보니까...
            #방향 감각이 일반인들이랑 반대가 되었어...
def vertical(x, y, v, mapper, another):
    if(v<0):
        for i in range(y-1, -1, -1):
            if(mapper[i][x] == 'O'):
                return -1
            elif(mapper[i][x] == '#'):
                return i+1
            elif(i == another[1] and x == another[0]):
                return i+1
    else:
        for i in range(y+1, n, 1):
            if(mapper[i][x] == 'O'):
                return -1
            elif(mapper[i][x] == '#'):#직전값 반환
                return i-1
            elif(i == another[1] and x == another[0]):
                return i-1

find(r.copy(), b.copy(), mapper, 1, 0)
find(r.copy(), b.copy(), mapper, 1, 1)
find(r.copy(), b.copy(), mapper, 1, 2)
find(r.copy(), b.copy(), mapper, 1, 3)


if(answer == 100):
    print(-1)
else:
    print(answer)

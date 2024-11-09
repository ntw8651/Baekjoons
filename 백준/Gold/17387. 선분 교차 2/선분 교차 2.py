#날먹을 위해 나 여기 등장
#아니 근데 이거에다가 유니온 파인드 하나 섞었다고 티어가 플레로 오른다고?
#플레는 2개 3개씩 섞는 느낌이구나~


#아니 근데 이건 예제 겁나 많이 주네!!!
#아까 그문제도 예제 쫌 마니 줄 것이지... 나뻣ㅅ다;;;
#아 원래 순서대로 풀라고 있던...걸까?
#뭣???? 나니???
#어...내가 모르는 뭔가...가 있나?
def checkAngle(ax, ay, bx, by, cx, cy):
    ans = (bx - ax) * (cy - by) - (by - ay) * (cx - bx)
    if(ans==0):
        return 0
    elif(ans > 0):
        return 1
    else:
        return -1

    
def check(fx, gx):
    '''
    선 A CCW -> B 점 방향 같 : 안겹침 -> 대신 둘다 0이고 하나라도 포함되면 겹침
        or -> B 점 방향 다르다 -> 만약 하나가 0이면 그 하나가 두 선 사이에 포함될 경우
                                        -> 겹침
                                        -> 아니면 안겹침
        -> 둘 모두 0이 아니고,
        -> 방향이 다르다면, 선 B CCW -> A 점 방향 같 : 안겹침
        -> B에서도 방향이 다르다면 -> 겹침

    직선상에 존재할 때, 겹치는 지 여부는 어떻게 확인하는가?
    -> "사각형"범위를 잡고, 그 안에 다른 점이 포함되어 있는 지 확인하면 된다
    -> 사각형 범위여도 괜찮은 이유 = 기울기는 정해져 있기 때문, 즉 x1 -> x2; y1 -> y2까지의 존재를 파악 가능하다는
    그런 말
    #어라... 세 점이 일직선상에 있어도 괜찮아야 하는데?
    머가 또 문제지

    이게 진짜 선분 교차구만... 
    '''
    f1 = checkAngle(fx[0], fx[1], fx[2], fx[3], gx[0], gx[1])
    f2 = checkAngle(fx[0], fx[1], fx[2], fx[3], gx[2], gx[3])
    if(f1 != f2):
        up = max(fx[1], fx[3])
        down = min(fx[1], fx[3])
        if(f1 == 0):
            if(fx[0] <= gx[0] <= fx[2] and down <= gx[1] <= up):
                return 1
            else:
                return 0
        if(f2 == 0):
            if(fx[0] <= gx[2] <= fx[2] and down <= gx[3] <= up):
                return 1
            else:
                return 0

        g1 = checkAngle(gx[0], gx[1], gx[2], gx[3], fx[0], fx[1])
        g2 = checkAngle(gx[0], gx[1], gx[2], gx[3], fx[2], fx[3])
        if(g1 != g2):
            if(g1 == 0 or g2 == 0):
                up = max(gx[1], gx[3])
                down = min(gx[1], gx[3])
                if(g1 == 0):
                    if(gx[0] <= fx[0] <= gx[2] and down <= fx[1] <= up):
                        return 1 
                    else:
                        return 0
                if(g2 == 0):
                    if(gx[0] <= fx[2] <= gx[2] and down <= fx[3] <= up):
                        return 1
                    else:
                        return 0
            else:
                return 1
        else:
            return 0
    else:
        if(f1 == 0):
            up = max(fx[1], fx[3])
            down = min(fx[1], fx[3])
            if((fx[0] <= gx[0] <= fx[2] and down <= gx[1] <= up) or (fx[0] <= gx[2] <= fx[2] and down <= gx[3] <= up)):
                return 1
            
            up = max(gx[1], gx[3])
            down = min(gx[1], gx[3])
            if((gx[0] <= fx[0] <= gx[2] and down <= fx[1] <= up) or (gx[0] <= fx[2] <= gx[2] and down <= fx[3] <= up)):
                return 1
        return 0

f = list(map(int,input().split()))
if(f[0] > f[2]):
    f = [f[2], f[3], f[0], f[1]]
g = list(map(int,input().split()))
if(g[0] > g[2]):
    g = [g[2], g[3], g[0], g[1]]

print(check(f,g))
#아니 이렇게 한 문제로 3문제를 날먹해도... 괜찮을 걸까? 다른 문제들은 그만 봐야겠다;; 이거
#문제 유형 보고 푸는 게 리얼 사기네...
#아니 그럼 이게 여기선 못 통과하는데 저기서 통과한 게 있다고?
#이거 반례로 데이터 추가 요청 해야할지도..?
#잠깐...설마... 반대로 했을 때에는 넘어가는 그런 게 있나...?
    #습; 이것도 아닌뎅 진짜 뭐임 그럼 앞선 문제는...어케... 풀린거?

#ㅋㅋㅋㅋㅋㅋㅋ 아니 0 0 3 3 -> 0 0 3 3을 안겹쳤다고 출력해버리네? 아니 5 5 3 3 5 5 3 3만인
    #어? 거꾸로 하는 걸 안쳐준다고?
#ㅋㅋㅋㅋㅋㅋㅋㅋ아 생각해보니까 x를 안바꿔 줬잖아!!!!!!ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    #아 진짜 짱나네ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#얼라리 또 뭐가 문제야 앗 오
'''
음음 union find 베이스에
대충 3000이니까 n^2으로다가 겹치는 선분 찾고
해주면 되겠네

그럼 이제 두 선분이 주어졌을 때,
겹치는 지 판단하는 알고리즘만 얻으면 쉽게 풀리겠어
교차하는 선분은 점 하나씩 교환했을 때,
무조건 교차하지 않는다.

교차하지 않는 선분은 점 하나씩 교환했을 때,
무조건 교차한다.


교차하지 않는 상태에서 y가 더 큰 점끼리 이으고, 작은 점끼리 이으면
사각형이 된다.
근데 교차한 상태면 모래시계가 된다

그냥 방정식 넣어서 해를 구해야 하나?
오..? 잠만 방정식 만드러봄. 근데 이걸 방정식?이라 하나? 함수?라? 하나?
진짜 수학 개몬ㅌ타네;;ㅎㅎ;;
대충
우선 함수를 구하기 위해선 기울기를 얻는다. 단 x1, x2 값이 같을 경우... 엄 일단 둬
(y1 - y2)/(x1 - x2)
기울기를 얻은 후 값 대입으로 절편을 구한다
y1 - (y1 - y2)/(x1 - x2) * x = b
그럼 끝
근데 만약 x1, x2가 같다면 그건 y축에 평행한 것이고
음... 그냥 따로 값을 예외처리 해줘야 할 듯


f(x) = ax + b
g(x) = cx + d 가 될 것이고
교점을 구하기 위해선
ax + b - cx - d = 0
(a - c)x + b - d = 0 에 해당하는 x값이 있어야 하고,
이 x값은 어차피 둘 중 하나에 해당한다(선분 두개의 x값 범위 중 하나면 댐)
단,
- a-c = 0일 때, b - d = 0이면 겹친다
ㄴ위에서 b - d != 0 이라면 겹치지 않는다
- a-c != 0일 때, x = (d - b)/(a - c)를 할당받으며,
    이때 x의 값은 범위 이하이상이어야 한다.
    이에 해당하면 겹친다.
    범위 초과 미만일 경우 겹치지 않는다.

..?

리얼 머가 문제임?

????
기울기가 같을 때 -> 완료
기울기가 0(또는 무한)일 때 -> 완료
기울기가 다를 때 -> 완료
?? 또 뭐가 있는데

'''
import sys
input = sys.stdin.readline


n = int(input())
parents = [i for i in range(n)]
value = [1 for i in range(n)]
lines = [[] for i in range(n)]
#여기서 등장 가능한 가장 큰 기울기 값은
#-5000에서 5000까지  1만이므로 대략 10만을 INF값으로 설정
INF = 1000000

for i in range(n):
    a, b, c, d = map(int,input().split())
    if(a < c):
        lines[i] = [a, b, c, d]
    else:
        lines[i] = [c, d, a, b]

def checkAngle(ax, ay, bx, by, cx, cy):
    #선ab와 점 c
    '''
    외적... 기하 때 배웠던 거 초기화 해버렸네 ㅎㅎ;;; 재송합니다 기하 및 고급수학 선생님..
    오 이거 쫌 기억 나는 것 같아
    그 뭐지 아닌데 그 분모가 0이면 없다 라는 그거 있짜나;;; 그 머냐;;
    아ㅋㅋㅋㅋㅋ 이거 분명 저번학기 이산수학에서도 배운건ㄷ게
    미치겟 아 ㅋㅋㅋㅋㅋ a->b면 b-a여야하지 참 진짜 기하 개더럽다ㅋㅋㅋㅠㅠㅠ
    a-b : bx- ax, by - ay
    b-c : cx- bx, cy - by

    외적 : 
    (bx - ax) * (cy - by) - (by - ay) * (cx - bx)

    ?잠만 식이 잘못된 것 가틍ㅇ데?
    어 잠만 이러면 하나는 직선이고 하나는 한쪽일 수 있잖아 음
    아 이것도 그냥 다른거라고 처리해주면 되겠구나
    어차피 하나만 직선이면 걘 반대에서 처리했을 때
    직선이 나올 수가 없으니까!...?
    서로 하나씩 직선일 가능성이 있냐고? 습... 없네! 없어 그런 경우는
    '''
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
    '''
    f1 = checkAngle(fx[0], fx[1], fx[2], fx[3], gx[0], gx[1])
    f2 = checkAngle(fx[0], fx[1], fx[2], fx[3], gx[2], gx[3])
    if(f1 != f2):
        #f직선 검사. 둘 중 하나만 직선
        #근데 하나만 직선이고 하나는 직선이 아닌데,
        #직선인 녀석이 포함되지 않을 경우
        #무조건 사망
        up = max(fx[1], fx[3])
        down = min(fx[1], fx[3])
        if(f1 == 0):
            #놀라운 사실 부호를 이따구로 해도 된다.. 왜?? 업뎃...된건가?
            #원래...이랬나??
            if(fx[0] <= gx[0] <= fx[2] and down <= gx[1] <= up):
                return 1
            else:
                return 0
        if(f2 == 0):
            if(fx[0] <= gx[2] <= fx[2] and down <= gx[3] <= up):
                return 1
            else:
                return 0
        #아니 무슨 구체 평면에서 만나는 것도 아니면서 왜 이따구
        g1 = checkAngle(gx[0], gx[1], gx[2], gx[3], fx[0], fx[1])
        g2 = checkAngle(gx[0], gx[1], gx[2], gx[3], fx[2], fx[3])
        if(g1 != g2):
            if(g1 == 0 or g2 == 0):
                up = max(gx[1], gx[3])
                down = min(gx[1], gx[3])
                #어 그럼 저걸 어케 차단하지
                #아 그냥 x도 제한주고 y도 제한주면 사각형이 생기고
                #그 안에서는 당연히 직선이니까 기울기 따라 이동하기 때문에
                #되겠구낭~
                if(g1 == 0):
                    if(gx[0] <= fx[0] <= gx[2] and down <= fx[1] <= up):
                        return 1
                    else:
                        return 0
                elif(g2 == 0):
                    if(gx[0] <= fx[2] <= gx[2] and down <= fx[3] <= up):
                        return 1
                    else:
                        return 0
            #는 개뿔 이게 문제였네!! T자형태로 만나는거야
            #어? 아닌데 그럼 문제가 아니구낭ㅎㅎ;;;
            #어? 아니 잠만 맞잖아 맞네 머 가 문 젠 데
                    #아 니 또 뭐 가 문 젠 데
                    #아!!!!!!!!!!
                    #찾았다!!!!!!!!!
                    #x값 범위로만 판다낳니까 그런거야!!!!!!!
                    #왜냐면 저런 경우!!! 1을 줘버리고 말아!!!
            else:
                return 1
        else:
            return 0#잠만 근데 하나만 직선이면 절대 겹칠 수가 없는데?
            #아 아니지 하나만 직선인 때에한 점이 포함되어 있으면 가능하구나
            #그럼 뭐 그냥 둬도 되겠다
            #어차피 둘이 다르단 거잖아 그것도 아 이게 겹치는 점이
            #안에 있어야지만 맞고 아니면 아닌데
        #음 머가 문제지
    else:
        if(f1 == 0):
            #둘다 겹치는 경우
            #자 여기는 어케해주지
            up = max(fx[1], fx[3])
            down = min(fx[1], fx[3])
            if((fx[0] <= gx[0] <= fx[2] and down <= gx[1] <= up) or (fx[0] <= gx[2] <= fx[2] and down <= gx[3] <= up)):
                #포함되면 아, 얘가 포함될 수 있지만, 반대로 쟤가 얠 포함할 수도 있잖아
                return 1
            
            up = max(gx[1], gx[3])
            down = min(gx[1], gx[3])
            if((gx[0] <= fx[0] <= gx[2] and down <= fx[1] <= up) or (gx[0] <= fx[2] <= gx[2] and down <= fx[3] <= up)):
                return 1
        return 0
    
def find(x):
    if(parents[x] == x):
        return x
    parent = find(parents[x])
    parents[x] = parent
    return parent

def union(a, b):
    pa = find(a)
    pb = find(b)
    if(pa == pb):
        return 0

    #개수 뺏어오고
    value[pa] += value[pb]
    parents[pb] = pa#d아!!! 잠만 여기 a가 아니라 pa여야 하는 거 아닌가?
    #어...아닌가?
    #a여도 상관없긴...하지 어 으음 그렇네
    #근데 이래야지 이제 시간초과가 안난다거나 설마 그런
    return 0


#생각해보니까 봤던 애 또 볼 필요가 있나?
#어차피 한 번 비교했던 애니까 볼 필요 없겠지
#습... 두번씩 봐볼까...?
#그럼 놓쳤던 애들이 잡힐 수도 있지...않을까?
for i in range(n):
    for j in range(n):
        if(i != j):
            if(check(lines[i], lines[j])):
                union(i, j)
        

maxi = 0
count = 0
for i in range(n):
    if(i == parents[i]):
        count+=1
        if(value[i] > maxi):
            maxi = value[i]
print(count)
print(maxi)

'''
와 이랬는데 알고보니 유니온 파인드 부분에서 시간초과 났던거면 진짜 재밌겠따 그죠

그래서... CCW...이걸 머 어케 쓰는걸까...
일단 머 이건 나누기 없이 곱하기만으로 이루어져 있다보니까
정확도 문제는 없나보구나

아 그래 이게 그 선 4개가 주어졌을 때 어...

일단 다른 두점에 대해서 CCW를 때려서 둘이 같은 게 나오면
 절대 안겹침
둘이 다른 게 나오면 다른 한 선에서도 CCW를 때려서 같은 게 나오는지 확인
그러니까

으아아아아악!!! 또 뭐지


'''




import sys
import math
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n = int(input())
users = [0 for i in range(86401)]
reusers = [0 for i in range(86401)]
reuser = 0
famous = [0 for i in range(86401)]
for i in range(n):
    start, end = input().rstrip().split(' - ')
    sa, sb, sc = map(int, start.split(':'))
    
    ea, eb, ec = map(int, end.split(':'))
    if(sa*60*60 + sb*60 + sc <= ea*60*60 + eb*60 + ec):
        users[sa*60*60 + sb*60 + sc] += 1
        users[ea*60*60 + eb*60 + ec + 1] -= 1 #전원 종료하는 그 순간에도 인기도 +

    else:#reverse 유저의 경우에 대해선... 거꾸로? 하면 되나? 아 모두가 켜져있다는 전제에서 시작하면 되겠구나
        reusers[ea*60*60 + eb*60 + ec + 1] -= 1
        reusers[sa*60*60 + sb*60 + sc] += 1
        reuser += 1
count = 0
for i in range(86400):
    count += users[i]
    famous[i] = count

for i in range(86400):
    reuser += reusers[i]
    famous[i] += reuser
'''
구간합, 그리고 여러번 구한다 = 세그먼트 트리

세그먼트 트리... 분명 1년 전에 무슨 특강에서
문제를 풀이해줬었는데
기억이 안ㄴ나네...

일단 대략 두배의 크기는 갖고 있어야겠지 당연히
트리구조는... 1번 인덱스에서 시작하고, 인덱스 곱하기 2는
하위 왼쪽 노드, 인덱스 * 2 + 1 는 오른쪽 노드였지.

범위 내이고, -1면 재귀함수로 가져오는 방식으로 가자
습
일단 좀 더럽게 구현해보고
깔끔한 구현 확인해보는 걸로

더해질 크기가 더 크면 쫑
아니잠깐, 어차피 트리를 만드는 건 그냥 for문으로 해도 되지 않을까?
음...아니 그냥 일단 하자
아 그럼 arr에서 마지막 애들이 들어갈 값만 미리 해주면 더 괜찮겠다
7개면 -> 8 -> log2, 3 -> 2**3 = 8
1
2 3
4 5 6 7
8 9 10 11 12 13 14 15

즉 15까지 있어야 하니까
아...아? 잠깐 생각해보니까 어차피 싹다 구해야하잖아
값 맨 뒤 지정할 것도 아니니까...

아니 무슨 자정을 넘어서 티비를 보냐?? 밤에는 티비를 보지마!!!

그럼 역방향은 따로 기록을...해줄까?
그래 역방향은 뭐 따로해도 괜찮겠지

아니잠깐, 그럼 이건 문제가 두개의 날짜에 대해서 그냥 똑같은 초로 지정해야하는건가?

'''
tree = [-1 for i in range(600000)]

for i in range(431072):
    tree[131072 + i] = 0

for i in range(86401):
    tree[131072 + i] = famous[i]


def getChild(now):#현위치, left부터 right, 현재 크기단위
    '''
    n : 현재 값을 기록할 node
    size : 현재 크기 단위
    adder : 더해질 크기
    '''
    if(tree[now] == -1):
        tree[now] = getChild(now*2) + getChild(now*2+1)
    return tree[now]

getChild(1)
#사이즈는 반토막씩
#pos에서 size까지. size처음 값은 131072
def getSum(now, pos, size, left, right):
    summation = 0
    if(now >= 299999):
        print(now, left, right, pos, size)
    if(tree[now] == 0):
        return 0
    if(left > pos+size or right < pos):
        return 0
    
    if(left == pos and pos+size == right):
        return tree[now]
    else:
        summation += getSum(now*2, pos, size//2, max(left, pos), min(right, pos+size//2))
        summation += getSum(now*2+1, pos+size//2+1, size//2, max(left, pos+size//2+1), min(right, pos+size))
        #이게 좀 자르는게 이상한가
        #0 131072
        #0 65536 / 65537 65536+65537
        #0 8이면
        #0 ~ 3
        #4 ~ 7...인덱스를 차지해야 하는..어?
        #애초에 뭔가... 이상한데

        return summation

q = int(input())
for i in range(q):
    start, end = input().rstrip().split(' - ')
    a, b, c = map(int, start.split(':'))
    left = a*60*60 + b*60 + c
    a, b, c = map(int, end.split(':'))
    right = a*60*60 + b*60 + c
    if(left <= right):
        print("{0:.10f}".format(getSum(1, 0, 131071, left, right) / (right - left + 1)))
    else:
        print("{0:.10f}".format((tree[1] - getSum(1, 0, 131071, right+1, left-1)) / (86400-(left - right -1))))

#어...이게 그러니까 전체 시간에서 딱 그시간대 
'''

1 2 3 4 5 6 7
에서
left 5
right 3였으면
4-4 값을 전체에서 빼고,
어...근데
3 4였다면?


'''


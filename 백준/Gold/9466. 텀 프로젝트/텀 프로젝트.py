import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
t = int(input())

'''
재귀를 가르키면 죽는다
재귀를 가르키는 애를 가르키면 죽는다
재귀를 가르키는 애를 가르키는 애를 가리키면 죽는다...

visited를 초기화하지 않는 방법으로 가면 시간초과 해결할 듯
'''
#아 한바퀴를 쭉 돌아야만 가능한거구나
#새로 끼어드는 애들은 친구로 안쳐주는...구나...쫌..슬플지도...
def find(now, arr, visited):#생각해보니까 그냥 순환인걸 체크하고
    #전체에서 빼는 게 더 빠를...지도...
    #arr -1은 이미 죽어버린 순환.
    #arr이 -1이 아니라면 살아있는 순환.
    global count
    if(visited[now] and arr[now] != -1):
        arr[now] = -1
        return now
    if(arr[now] == -1):
        return -1
    
    visited[now] = 1
    result = find(arr[now], arr, visited)
    arr[now] = -1
    if(result == -1):
        count += 1
        return -1
    elif(result == now):
        return -1
    else:
        return result
    #중복이 어디서 발생하지
    #많아봤자 20만번인데
    '''이러면 4개가 떠야하는데 따라 죽지를 않네?
    5
    2 3 4 5 5
    순간 유튜브에 빠져버릴 뻔...

    그냥... visited 대략 초기화하면서... 못 돌아오는 애들만 다 날려주면 되는 거
    아닌가...
    아니지 visited초기화 할 필요도 없이 중간에 연결되면 걔네끼리만 연결해주면 되네

    아 새로운 visited로 해줘야 되겠네 그래야 현재 순회인지 알 수 있으니까
    '''
    #잠만, visited를 초기화할 필요가 있나?
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0 for i in range(n+1)]
    count = 0
    for i in range(1,n+1):
        if(arr[i] != -1):
            find(i, arr, visited)
            #print(visited, arr, count)
    print(count)
    #얘도 뭐 그냥 지칭하는 애들 쭉 따라가면서
    #잠깐, 근데 이건 그냥 자칭하는 애들만 골라내면 되는 거 아닌ㄱ
    #아 자칭하는 애를 칭하는 애들이 안되는 거구나
    #아니 근데 1이 3이랑 하고 싶다는데 좀 시켜줘라;;
    #어? 자칭하는 애는 혼자 팀이 된다고?
    #아 자칭하는 애가 꼭대기에 있는 팀은 망하는구나
    #따라가다가 자칭하는 애를 만난다 -> 싹다 -1로 돌리기(자칭빼고)
    #따라가다가 회문이 되었다 -> 팀이니까 괜춘
    #마지막에 -1개수 세기 오키 이거면 되겠
    #이건 무한회문 발생인가 아 first가 아니고 중간에 끼일 수 있구나
    #그럼 중간에 낀 친구는 조원이 될 수 있나? 있지
    #어라리 머지
    

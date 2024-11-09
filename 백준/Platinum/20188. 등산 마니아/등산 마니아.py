import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
roads = {}
ans = 0
#아무튼 오늘 할 것~
#R E V E N G E
for i in range(n-1):
    s, e = map(int, input().split())
    if(s not in roads):
        roads[s] = []
    if(e not in roads):
        roads[e] = []
    roads[s].append(e)
    roads[e].append(s)

#완전이분그래프 인데...뭐...
def find(now, parent, length):
    global ans
    #가장 끝, leaf  노드일 때 정상으로부터 거리 반환
    if(len(roads[now]) == 1 and roads[now][0] == parent):
        return length, 1
        
    childCounts = []
    childVals = []
    for i in roads[now]:
        if(i != parent):
            v, c = find(i, now, length + 1)
            childVals.append(v)
            childCounts.append(c)

    #부모랑 자식 값도 그냥
    #자식 전체값 더해주면 되네

    #아 그러네... 다 다른 자식이면 결국 300 000^2가 되어버리는구나
    #아? 그럼 그냥 전체 값에서 자기만 뺀 애를 하면 되잖아?
            
    #다른 선에서 온 자식끼리 서로 더한 값들 올려주고(서로 가는 길이)
    #자신과의 거리는 그냥 자식 length더해주기
    childCount = len(childCounts)
    allCount = 0
    allVal = 0
    
    for i in range(childCount):
        allCount += childCounts[i]
        allVal += childVals[i]

    #재활용하기 위해 뽑아두기
    resultV = allVal
    resultC = allCount
    
    for i in range(childCount):
        allCount -= childCounts[i]
        allVal -= childVals[i]
        ans += childVals[i] * allCount  + allVal * childCounts[i] - length * childCounts[i] * allCount
        
        ans += childVals[i]#부모 - 자식 거리
    #생각해보니까 이렇게 풀면 300 000이니까 무조건 시간초과겠구나
    #300 000개가 하나씩 연산만 해도 n^2인데
    #child하나로 통합해서 올려주기
    #자기 부모까지의 거리를 더해서 올려줄까
    #그러니까 결국 자기 부모랑은 연산을 해야하잖아? 그걸 미리해서 대입해두는거지
    #31점이면 4번 5번만 통과한건가
    #그러네 결국 시간초과가 문제구ㅏ
    #특히 배열을 다뤄서 더 그런 것 같네
    #그럼 length는 산하 자식 개수만큼 증가하는건가 그치
    #잠깐, 생각해보니까 왼쪽 아이들 값 전체 합친거랑 오른쪽 애들 값 전체 합친거
    #에서 그냥 부모 length*아이들 개수곱 만 빼주면 되는거네? 배열이 필요없구나
    resultV += length #자신 값
    resultC += 1 #자신 
    #print(resultV)
    
    return resultV, resultC
    
find(1, -1, 0)
print(ans)

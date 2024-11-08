from os import sys
from heapq import heappush, heappop

input = sys.stdin.readline


N = int(input())
M = int(input())

INF = 2**32-1
city = [[] for i in range(N)]


for i in range(M):
    s, e, c = map(int, input().split())
    city[s-1].append([e-1, c])    

s, e = map(int,input().split())
#일단 무지성 파이파
priorQue = []

cityCost = [INF for i in range(N)]
#어딘가 약간 쓸모 없는게 있는듯?
    #거리가 우선순위지?
cityCost[s-1] = 0
heappush(priorQue, (cityCost[s-1], s-1))
#print(priorQue)

visited = [False for i in range(N)]


#node 0 : Distance // 1: Number
#i(city) 0 : EndPoint // 1 : Distance
 #fhehwieufhwaiuef asdfja오ㅑㅐ ㅐ왜왜왜왱애ㅗ애오옹왜애왜왜왜안되는거지?
#잠깐 그럼 내가 원래 했던 방식은 뭐지? 딱히 최소를 고르지도 않고
#싹다 업데이트하면서 갔잖아 
while(priorQue != []):
    #print(priorQue) 이미 처리되었으므로 무시한다? 이미 처리되었는지 어케알아?
    #방문 bool을 해둬야해? 근데... 한번만 가는 건 아니잖아? 아 아니네
    node = heappop(priorQue)
    if(not visited[node[1]]):
        for i in city[node[1]]:
            #print(i)
            if(cityCost[i[0]] > node[0] + i[1]):
                cityCost[i[0]] = node[0] + i[1]
                heappush(priorQue, (cityCost[i[0]], i[0]))
    visited[node[1]] = True

    
print(cityCost[e-1])

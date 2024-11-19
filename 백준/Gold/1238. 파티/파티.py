'''
하나는 거꾸로 길 선정
'''
import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m, x =map(int,input().split())
INF = 10**10
roads = [[INF for i in range(n+1)] for j in range(n+1)]
goCosts = [INF for i in range(n+1)]
comeCosts = [INF for i in range(n+1)]
resultCosts = [0 for i in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    roads[a][b] = c


visited = [0 for i in range(n+1)]
heap = [(0,x)]
count = 0
while(heap and count <= n):
    a = heapq.heappop(heap)
    #print("asdf")
    #print(heap)
    if(visited[a[1]]):
        continue
    else:
        goCosts[a[1]] = a[0]
        visited[a[1]] = 1
        count += 1
        for i in range(1, n+1):
            if(roads[a[1]][i] != INF and not visited[i]):
                heapq.heappush(heap,(a[0]+roads[a[1]][i], i))

#print("@")
visited = [0 for i in range(n+1)]
heap = [(0,x)]
count = 0
while(heap and count <= n):
    a = heapq.heappop(heap)
    #print("asdf")
    #print(a, "#", heap)
    if(visited[a[1]]):
        continue
    else:
        comeCosts[a[1]] = a[0]
        visited[a[1]] = 1
        count += 1
        for i in range(1, n+1):
            if(roads[i][a[1]] != INF and not visited[i]):
                heapq.heappush(heap,(a[0]+roads[i][a[1]], i))



'''
습 다익스트라마냥 해야하나
어라 근데 다익스트라가 원래 골드 3정돈가?
어 근데 이게 다익스트라가 맞나? 다익스트라가 뭐였찌
'''

for i in range(1, n+1):
    if(goCosts[i] == INF):
        goCosts[i] = 0
    if(comeCosts[i] == INF):
        comeCosts[i] = 0
    resultCosts[i] = goCosts[i] + comeCosts[i]
    

print(max(resultCosts))



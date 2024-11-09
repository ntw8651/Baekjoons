#안 쉬워..!
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, r, q = map(int, input().split())
roads = {}
visited = [0 for i in range(10**5 + 1)]
values = [0 for i in range(10**5 + 1)]
for i in range(1, n+1):
    roads[i] = []

for i in range(n-1):
    s, e = map(int,input().split())
    roads[s].append(e)
    roads[e].append(s)

#답 미리 다 구해놓기 아 자기도 해당이구나
def find(now, visited, values):
    value = 0
    for i in roads[now]:
        if(visited[i] == 0):
            visited[i] = 1
            value += find(i, visited, values)

    values[now] = value+1#잠깐, 서브트리면 미포함 아닌가? 아 자기도 포함으로 치는구나
    return values[now]
visited[r] = 1
find(r, visited, values)

for i in range(q):
    u = int(input())
    print(values[u])

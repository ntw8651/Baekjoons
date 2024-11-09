#가장 값싼 간선부터
#이건 유니온 파인드 or 최소힙 둘 중 하나는 써야하는 문제구나
#왜냐면 크루스칼 알고리즘이랑 프림 알고리즘이 있으니까.
#아니 최소힙도 필요 없네 생각해보니까

import sys
input = sys.stdin.readline
v, e = map(int ,input().split())
edges = []

#딕셔너리로 저장하고 돌리자
visited = [0 for i in range(v+1)]

queue = []
for i in range(e):
    s, e, t = map(int,input().split())
    edges.append([s,e,t])

edges.sort(key = lambda x : x[2])

count = 0
time = 0
#양쪽이 방문한 게 아니면 괜춘
#양쪽 다 방문한 거면 X
#아 반대 방향으로 연결될 수가 있구나 생각해보니까...가 아닌데?
#그럼 visited가 안켜져있어야 하는데?
#아 생각해보니까 섬끼리 연결이 되어야 하는구나
#결국엔 최소힙이든 유니온 파인드든 필요한 거였구만...
#visited를 부모로 하자

def find(x):
    if(x == visited[x]):
        return x
    else:
        visited[x] = find(visited[x])
        return visited[x]

for i in edges:
    #둘다 부모 없 : 하나는 자기자신, 하나는 부모로 연결
    #한 명 부모 있 : 부모 있는 애의 부모로 연결
    #둘 다 부모 있 : 한 쪽 전체를 편입시키기
    if(i[0] == i[1]):
        continue

    #P0 = find(i[0])
    #P1 = find(i[1])
    if(visited[i[0]] == 0 and visited[i[1]] == 0):#둘다 고아
        visited[i[0]] = i[0]
        visited[i[1]] = i[0]
        count+=1
    elif(visited[i[0]] != 0 and visited[i[1]] != 0):#둘다 부모있
        P0 = find(i[0])
        P1 = find(i[1])
        if(find(i[0]) == find(i[1])):
            continue
        else:
            visited[P1] = P0
            count+=1
    else:#하나만
        if(visited[i[0]] != 0):#왼쪽이 부모 있
            visited[i[1]] = find(i[0])
        else:
            visited[i[0]] = find(i[1])
        count+=1
    time += i[2]
        
    if(count == v-1):
        break

print(time)

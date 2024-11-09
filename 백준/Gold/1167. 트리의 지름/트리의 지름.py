import sys
#머지 왜 recursion 설정 안했지
#재채점 되면서 나가리 된건가??
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
tree = {}
visited = [0 for i in range(100001)]#공용 방문
maxDist = 0

'''
그 점까지 오는 최대값을 저장하고,
두 최대값의 합을 max와 비교

연결 간선을 어떻게 저장하지?
10만 * 10만이라 배열은 안될 것 같은

그래서 결국 dict쓰려하는데 음 아니 어차피 다보려면 배열에다가 저장하면 되는구나?

대충 동적 배열 느낌 문제구
'''

n = int(input())

tree = [[] for i in range(100001)]
#입력부
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(1, len(k)-1, 2):
        tree[k[0]].append([k[j],k[j+1]])
         



def getDist(n, visited):
    global maxDist
    visited[n] = 1
    fst = 0
    scd = 0
    
    for i in tree[n]:
        if(visited[i[0]] == 0):
            vDis = getDist(i[0], visited) + i[1]
            if(vDis>fst):
                scd = fst
                fst = vDis
            elif(vDis>scd):
                scd = vDis

    if(maxDist < fst+scd):
        maxDist = fst+scd
    
    return fst



getDist(1, visited)
print(maxDist)

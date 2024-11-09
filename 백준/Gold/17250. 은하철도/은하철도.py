'''
유니온 파인드에 결과에 값 더해주기 ㅇㅋ

'''
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
planet = [0 for i in range(n+1)]

def find(x):
    if(parent[x] == x):
        return x
    result = find(parent[x])
    parent[x] = result
    return result

def union(a, b):
    #왼쪽을 오른쪽으로 합치고 반환은 왼쪽 행성의 수
    aa = find(a)
    bb = find(b)
    if(aa != bb):
        planet[aa] += planet[bb]
        parent[bb] = aa

    return planet[aa]


for i in range(1, n+1):
    planet[i] = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(union(a, b))

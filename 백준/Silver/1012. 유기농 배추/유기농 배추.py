'''
1. 칸마다 검사
2. 1일 경우
2-1 상, 하, 좌, 우 재귀함수 돌려서 다지우기 그리고 count +1
3. 출력
'''
import sys
sys.setrecursionlimit(10**6)


def find_friends(x, y):
    global farm
    farm[y][x] = '0'
    
    if(farm[y][x+1] == '1'):
        find_friends(x+1, y)
        
    if(farm[y+1][x] == '1'):
        find_friends(x, y+1)

    if(farm[y][x-1] == '1'):
        find_friends(x-1, y)

    if(farm[y-1][x] == '1'):
        find_friends(x, y-1)


T = int(input())


for test in range(T):
    count = 0
    M, N, K = map(int, input().split())
    farm = []
    for i in range(N+2):
        farm.append(['0']*(M+2))
    
    for i in range(K):
        x, y = map(int, input().split())
        farm[y+1][x+1] = '1'
        

    for p in range(N):
        for q in range(M):
            if(farm[p+1][q+1] == '1'):
                count += 1
                find_friends(q+1, p+1)

    print(count)

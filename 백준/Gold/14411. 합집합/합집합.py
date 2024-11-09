import sys
input = sys.stdin.readline
n = int(input())
points = []
for i in range(n):
    x, y = map(int,input().split())
    points.append([x//2, y//2])

points.sort(key = lambda x : (-x[0], -x[1]))

#한 사분면만 보고 곱하기 4해주면 됨
#오른쪽 상단부터 보기
nowX = 10**8
nowY = 0
ans = 0
for i in points:
    if(nowX == i[0]):
        continue
    if(i[1] > nowY):
        ans += i[0] * (i[1] - nowY)
        nowY = i[1]
        
    nowX = i[0]
    
print(ans*4)

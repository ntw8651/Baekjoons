'''
기울기를 따져서 직각인지 체크
아니그냥 피타고라스 때리면 되는거잖아
소수점때매 안된다고 생각했는데 어차피 직각이면 ==체크니까
루트 안 취해줘도 되는구나...
루트에 취한다~

안이 시간초과 화가 나는 부분이에요
내 플레 진급을 막지마!!!
'''
import sys
input = sys.stdin.readline
n = int(input())
points = []
pa= points.append 
for i in range(n):
    pa(list(map(int,input().split())))


def check(x1, y1, x2, y2, x3, y3):
    #기울기
    lefty =  y2 - y1
    leftx = x2 - x1
    righty = y3 - y1
    rightx = x3 - x1
    middlex = x3 - x2
    middley = y3 - y2

    lefty *= lefty
    leftx *= leftx
    righty *= righty
    rightx *= rightx
    middlex *= middlex
    middley *= middley

    if(lefty+leftx+righty+rightx == middlex+middley):
        return 1
    if(lefty+leftx+middlex+middley == righty+rightx):
        return 1
    if(middlex+middley + righty+rightx == lefty+leftx):
        return 1
    return 0
    

ans = 0
for i in range(n):
    #세 점에서 해서 하나라도 참이면
    for j in range(i+1, n):
        for k in range(j+1, n):
            if(check(points[i][0],points[i][1], points[k][0],points[k][1], points[j][0],points[j][1])):
                #print("Asf")
                ans+=1
print(ans)

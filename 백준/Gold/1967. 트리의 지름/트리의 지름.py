#각 모든 부모에서
#아래로 내려가면서
#가장 긴 두 선을 찾는거지
#그냥 자식으로 내려가면서 return으로 최대값만 가져오게 하면 될듯
#그리고 본인에서 체크하는거지
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


tree = {}
n = int(input())
for i in range(n-1):
    s, e, t = map(int, input().split())
    if(s not in tree):
        tree[s] = {e : t}
    else:
        tree[s][e] = t

maximum = 0

def findEdge(now, value):
    global maximum
    #value = 원점부터 자기까지
    #
    #끝에 다다르면 자기 값 리턴
    #끝이 아니면 자식중에 가장 높은 값 리턴
    child = []
    try:
        for i in tree[now].keys():
            length = findEdge(i, tree[now][i])
            child.append([i, length])
    except KeyError:
        #맨 끝이라는 의미
        return value
    

    maxDist= 0
    secondDist = 0

    for i in child:
        if(i[1] >= maxDist):
            secondDist = int(maxDist)
            maxDist = i[1]
        elif(i[1] >= secondDist):
            secondDist = i[1]

    if(maxDist + secondDist > maximum):
        
        #print("asdf", now, maxDist, secondDist)
        maximum = maxDist + secondDist

    return maxDist + value

findEdge(1, 0)
print(maximum)

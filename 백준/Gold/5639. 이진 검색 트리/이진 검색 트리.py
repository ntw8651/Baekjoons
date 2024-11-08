import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
tree = [[-1, -1] for i in range(1000002)]

top = -1
# 그냥 반복문 돌려서 줘볼까
# 어니 먼데
                
def get(now):
    if(tree[now][0] != -1):
        get(tree[now][0])
    if(tree[now][1] != -1):
        get(tree[now][1])
    print(now)

inps = []
try:
    top = int(input())
    while(True):
        inp = int(input())
        pos = top
        while(True):
            if(inp < pos):
                if(tree[pos][0] == -1):
                    tree[pos][0] = inp
                    break
                else:
                    pos = tree[pos][0]
            elif(inp > pos):
                if(tree[pos][1] == -1):
                    tree[pos][1] = inp
                    break
                else:
                    pos = tree[pos][1]
except:
    exit

#음... 노드는 만개니까 그냥 recursion 1만 주자...
get(top)

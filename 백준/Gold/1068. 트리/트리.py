n = int(input())
nums = list(map(int, input().split()))
tree = [[] for i in range(n)]
root = 0
for i in range(n):
    if(nums[i] == -1):
        root = i
    else:
        tree[nums[i]].append(i)
drop = int(input())

def getChild(now):
    if(now == drop):
        return 0
    childs = 0
    for i in tree[now]:
        childs += getChild(i)
    if(childs == 0):
        return 1
    else:
        return childs

print(getChild(root))

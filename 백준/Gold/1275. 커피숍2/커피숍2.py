'''
아니 머임;;;
'''
import sys
input = sys.stdin.readline

n, q = map(int,input().split())

nums = list(map(int,input().split()))
tree = [0 for i in range(n*4)]


def MakeTree(left, right, index):
    if(left == right):
        tree[index] = nums[left]
        return tree[index]

    mid = (left + right)//2
    value = 0
    value += MakeTree(left, mid, index*2)
    value += MakeTree(mid+1, right, index*2+1)
    tree[index] = value
    return tree[index]

def GetTree(s, e, left, right, index):
    #s, e가 원래 얻고자 했던 구간
    if(e < left or right < s):
        return 0

    if(s <= left and right <= e):
        return tree[index]

    mid = (left + right)//2
    value = 0
    value += GetTree(s, e, left, mid, index*2)
    value += GetTree(s, e, mid+1, right, index*2+1)
    return value

def ChangeTree(target, dest, left, right, index):
    if(target < left or right < target):
        return 0

    if(left == right):
        if(left == target):
            origin = tree[index]
            tree[index] = dest
            return origin
        else:
            return 0

    mid = (left + right)//2
    modify = 0#아ㅋㅋㅋ
    modify += ChangeTree(target, dest, left, mid, index*2)
    modify += ChangeTree(target, dest, mid+1, right, index*2+1)
    tree[index] += dest - modify
    return modify

#아 설마 y는 x보다 작거나 같다는 걸 명시 안했으니까...?
MakeTree(0,n-1, 1)
for i in range(q):
    x, y, a, b = map(int, input().split())
    if(y < x):
        t = x
        x = y
        y = t
    print(GetTree(x-1,y-1, 0, n-1, 1))
    ChangeTree(a-1, b, 0, n-1, 1)


    

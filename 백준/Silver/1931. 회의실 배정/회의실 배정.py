import sys
input = sys.stdin.readline

n = int(input())
comp = []

ca = comp.append
for i in range(n):
    ca(list(map(int, input().split())))


comp.sort(key = lambda x : (x[1], x[0]))


count = 0
minT = -1

for i in comp:
    if(i[0] >= minT):
        count+=1
        minT = i[1]

print(count)

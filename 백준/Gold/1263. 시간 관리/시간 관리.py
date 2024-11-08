n = int(input())
works = []
for i in range(n):
    works.append(list(map(int,input().split())))

works.sort(key = lambda x : -x[1])

t = 10**10
for i in range(n):
    if(works[i][1] < t):
        t = works[i][1]
    t -= works[i][0]

if(t<0):
    print(-1)
else:
    print(t)

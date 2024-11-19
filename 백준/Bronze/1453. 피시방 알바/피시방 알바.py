n = int(input())
b = list(map(int, input().split()))
c = []
d = int(0)
for i in b:
    if(i in c):
        d+=1
    else:
        c.append(i)
print(d)

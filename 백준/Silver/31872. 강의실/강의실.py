n, k = map(int,input().split())
#가장 먼 거리들에서 순간이동

classes = [0] + list(map(int, input().split()))
#좌표랑, 다음 곳으로까지의 거리
times = []
classes.sort()
ta = times.append
for i in range(n):
    ta([classes[i], classes[i+1]-classes[i]])

times.sort(key = lambda x : -x[1])

time = 0
teleports = {}
for i in range(k):
    teleports[times[i][0]] = 1

for i in range(n):
    if(classes[i] not in teleports):
        time+=classes[i+1] - classes[i]

print(time)


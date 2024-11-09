a, b = map(int, input().split())
s, R, e, f = map(int, input().split())
g = 0
for i in range(a):
    ABC = input()
    g+=ABC.count('P')
    

if(e*f == g):
    print(0)
else:
    print(1)

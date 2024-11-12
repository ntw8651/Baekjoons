n = int(input())
inps = {}
for i in range(n):
    a, b = input().split()
    inps[b] = a

string = input()
ans = ''
for i in string:
    ans += inps[i]

l,r = map(int,input().split())
print(ans[l-1:r])

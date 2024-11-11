n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))


ans = 0
coins.reverse()
for i in coins:
    ans+=k//i
    k -= (k//i) * i

print(ans)
#이항계수... nCm, 아니 조합이자나?
n, m = map(int, input().split())
up = 1
down = 1
for i in range(m):
    up*=n-i
    down*=i+1

print(up//down)

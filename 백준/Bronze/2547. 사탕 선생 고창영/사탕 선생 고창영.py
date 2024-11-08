t = int(input())
for i in range(t):
    input()
    n = int(input())
    ans = 0
    for i in range(n):
        ans += int(input())%n

    if(ans%n == 0):
        print("YES")
    else:
        print("NO")

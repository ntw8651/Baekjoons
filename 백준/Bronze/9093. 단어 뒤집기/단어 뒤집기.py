t=int(input())
for _ in range(t):
    a=input().split()
    for i in a:
        for k in range(len(i)-1, -1, -1):
            print(i[k], end="")
        print(" ", end="")
    print()

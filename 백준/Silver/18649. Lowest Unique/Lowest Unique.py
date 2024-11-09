import sys
input = sys.stdin.readline
n, k, m = map(int,input().split())
for i in range(m):
    for j in range(1, k+1):
        print(j, end =" ")
    print()
    

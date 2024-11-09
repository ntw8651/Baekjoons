import sys
N, X = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
for i in T:
    if(i < X):
        print(i,end=' ')

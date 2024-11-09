t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    arr = []
    for i in range(a):
        arr.append(input())
    for i in range(a):
        print(arr[a-i-1])


n, h, w = map(int, input().split())
origin = ['?' for i in range(n)]
for i in range(h):
    inp = input()
    for j in range(n*w):
        if(inp[j] != '?'):
            origin[j//w] = inp[j]
print(''.join(origin))

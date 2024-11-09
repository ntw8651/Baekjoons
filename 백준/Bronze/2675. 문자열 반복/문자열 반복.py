T = int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    b = str(b)
    word = str('')
    for z in b:
        word+=z*a
    print(word)

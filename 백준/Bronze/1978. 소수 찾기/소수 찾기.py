a = int(input())
b = list(map(int, input().split()))
a = int(0)
d = bool()
for c in b:
    if(c != 1):
        d = True
        for i in range(2, c):
            if(c%i == 0):
                d = False
        if(d == True):
            a+=1
        
print(a)

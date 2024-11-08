count = 0
n = int(input())
for i in range(6, -1, -1):
    if(n>=2**i):
        n-=2**i
        count+=1
    
print(count)

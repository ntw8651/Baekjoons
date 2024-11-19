import sys
T = int(sys.stdin.readline())
def fac(num):
    a=int(0)
    for i in range(num+1):
        a+=i
    return(a)

for i in range(T):
    count = int(0)
    a,b = map(int, sys.stdin.readline().split())
    distance = b-a
    dob = True
    c = int(1)
    zxcv = int(0)
    while(True):
        if dob== True:
            count+=c
            dob=False
        else:
            count+=c
            dob=True
            c+=1
        zxcv+=1
        if(count>=distance):
            break
    print(zxcv)

cyclelen = int(0)
N = input()
M = N
a= int(0)
c = True
while(int(N) != int(M)or c == True ):
    if(int(M) < 10):
        M = '0'+str(int(M))

    M = str(M)
    M = str(M[1]) + (str(int(M[0]) + int(M[1]))[-1])
    cyclelen += 1
    c= False
    a+=1
print(cyclelen)

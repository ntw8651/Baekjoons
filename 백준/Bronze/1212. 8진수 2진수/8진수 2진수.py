n = input()


a = int(n[0])
q = a//4
w = (a-q*4)//2
e = (a-q*4)%2
print(int(q*100+w*10+e),end="")



for i in n[1:]:
    a = int(i)
    q = a//4
    w = (a-q*4)//2
    e = (a-q*4)%2
    print(q,w,e, sep = "", end="")

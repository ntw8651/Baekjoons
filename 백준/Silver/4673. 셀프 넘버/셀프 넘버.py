def d(n):
    ns = int(0)
    for i in list(str(n)):
        ns+=int(i)
    n=n+ns
    return(n)
c = []
b = []
a = 0
number = int(0)
while(number<10000):
    number = d(a)
    a+=1
    b.append(number)

for i in range(10000):
    c.append(i)
    
b = set(b)
b = list(b)

b = [x for x in c if x not in b]

for i in range(3):
    del b[-1]
for i in b:
    print(i)

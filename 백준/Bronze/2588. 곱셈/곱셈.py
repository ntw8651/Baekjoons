a = int(input())
b = list(input())
for i in b[::-1]:
    print(a * int(i))
print(a*((int(b[0])*100)+(int(b[1])*10)+(int(b[2]))))

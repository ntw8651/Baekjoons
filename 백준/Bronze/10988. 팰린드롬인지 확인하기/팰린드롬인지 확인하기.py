a = input()
check = True
for i in range(len(a)):
    if(a[i] != a[len(a)-i-1]):
        check = False
        print(0)
        break

if(check):
    print(1)


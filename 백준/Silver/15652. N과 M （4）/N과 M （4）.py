n, m = map(int, input().split())


def qwer(nowN, count, string):
    string += " " + str(nowN)
    #print(string, count)
    if(count >= m-1):
        print(string[1:])
        return
    for i in range(nowN, n+1):
        qwer(i, count+1, string)
        
    

for i in range(1, n+1):
    qwer(i, 0, "")

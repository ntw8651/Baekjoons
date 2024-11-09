T = int(input())

for t in range(T):
    total = int(0)
    k = int(input())
    n = int(input())
    list_list = []
    real_list = []
    for i in range(n):
        list_list.append(i+1)
        
    real_list.append(list_list)
    for i in range(k-1):
        real_list.append([1])

    
    for i in range(1, k):
        for p in range(1, n):
            c = real_list[i-1][p]+real_list[i][p-1]
            real_list[i].append(c)

    print(sum(real_list[-1]))
import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
max_b = max(b)
all_num = int(0)
for i in range(len(b)):
    all_num += b[i]/max_b*100

print(all_num/len(b))

    

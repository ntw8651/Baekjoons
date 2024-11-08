N = int(input())
num_list = []
count = 0 
def asdf(N):
    num = []
    for i in N:
        num.append(i-1)
        if(i%3==0):
            num.append(i//3)
        if(i%2==0):
            num.append(i//2)

    return num

#1이란 수가 나올때까지 반복
#이미 1이면
if(N != 1):
    num_list.append(N)
    while(min(num_list) != 1):
        num_list = asdf(num_list)
        count+=1
        

print(count)

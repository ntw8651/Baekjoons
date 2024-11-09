N, M = map(int, input().split())
line = []
count_list = [0]*M
count_listTT = [0]*M
line_count = [0]*N
line_temp = [0]*N

count = int(0)
for i in range(N):
    line.append(list(input()))
K = int(input())



while(line != []):
    line_count[count] = line.count(line[0])
    line_temp[count] = line[0]
    for i in range(line_count[count]):
        line.remove(line_temp[count])

        
        
    count +=1

ccount = int()
for i in range(count):
    ccount = 0
    for p in range(M):
        if(line_temp[i][p] == '0'):
            ccount+=1
    if(ccount > K):
        line_count[i] = 0
    elif((K - ccount)%2 == 1):
        line_count[i] = 0

print(max(line_count))
    
        
    



'''
K가 홀수일경우
0이 K보다 적고 같은 것 최대개수

K가 짝수일 경우
1이 K보다 적고 같은 것 최대개수

아 빈0의 개수의 배수인지 확인하면 되겠네

그럼 만들 알고리즈ㅡㅁ은
같은 모양 찾기

얘를 그냥 먼저해야지

'''
'''
for p in range(M):
    for q in range(N):
        if(line[q][p]=='0'):
            count_list[p]+=1


for q in range(N):
    for p in range(M):
        if(line[q][p]=='0'):
            count_listTT[p]+=1
    if(count_listTT[p]>K):
        count_listTT[p] = -1


for i in range(K):
    col = count_list.index(max(count_list))
    count_list[col] = N-max(count_list)
    for q in range(N):
        if(line[q][col]=='0'):
            line[q][col]='1'
        else:
            line[q][col]='0'

for i in range(N):
    if('0' not in line[i]):
        count+=1

print(count)
'''


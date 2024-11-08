N, M = map(int, input().split())
num = []
#기본적으로 가로세로1=1이라는 전제
size = 1


for i in range(N):
    num.append(list(map(str, input().split())))

for i in range(N-1):
    #각 수를 오른쪽 아래로 내리탐색
    #오른쪽 아래 같은 거리로 찾았을 시에 대각선 위치 확인
    #대각선도 맞을 경우에 크기 계산 후 입력
    #만약 해당 크기가 남은 길이최대보다 길경우 바로 break
    #이정도면 될듯
    for right in range(M-1):
        for down in range(i+1, N):
            if(M-right-1<down-i):#down이 남은 오른쪽 공간보다 크면 안된단 의미인
                break

            if(num[i][0][right] == num[down][0][right]):

                if(num[i][0][right] == num[i][0][right+(down-i)]):

                    if(num[i][0][right] == num[down][0][right+(down-i)]):

                        if(size<(i-down-1)**2):                        
                            size = (i-down-1)**2
                        #아?


print(size)

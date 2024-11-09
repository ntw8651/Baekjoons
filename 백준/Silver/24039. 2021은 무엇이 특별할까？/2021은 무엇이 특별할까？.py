#소수를 대~충 110까지 세운다 100*100이면 대~충 10000이니까 N보단 안클꺼아냐
#그다음 연속된 두 소수의 곱 리스트를 다시 세운다~
#그다음은 무한비교 끝

N = int(input())
allsu = [False,False] + [True]*110
sosu = []
sosuGob = []

for i in range(2, 111):
    if allsu[i]:
        sosu.append(i)
        for j in range(2*i, 111, i):
            allsu[j] = False

for i in range(len(sosu)-1):
    sosuGob.append(sosu[i]*sosu[i+1])

for i in sosuGob:
    if(i>N):
        print(i)
        break

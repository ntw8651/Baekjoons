import math
from decimal import Decimal, getcontext
#물론 반올림 해야하니까 7자리라고 해도 결국 백만만 돌리면 되네..?
a,b,c = map(int,input().split())
getcontext().prec = 28
def check(x):
    result = a*x+b*sin(x)-c
    return result

#팩토리얼 미리 계산
fact = [0 for i in range(100)]
fact[1] = 1
for i in range(2, 100):
    fact[i] = fact[i-1]*i

#테일러 급수로다가 쌈뽕난 sin값 구해버리기
sinPrec = 20
pi = Decimal('3.1415926535897932384626433')
def sin(x):
    x %= pi*2
    result = Decimal('0')
    for i in range(sinPrec+1):
        result += pow(-1,i) * pow(x, 2*i+1) / fact[2*i+1]
    return result#머지

count = 0
left = Decimal(0)
right = Decimal(1000000)
while(count<10000):
    mid = Decimal(left + right)/2
    result = check(mid)
    if(result == 0):
        break
    elif(result > 0):
        right = mid
    else:
        left = mid
    count+=1
    
print(round(mid, 6))


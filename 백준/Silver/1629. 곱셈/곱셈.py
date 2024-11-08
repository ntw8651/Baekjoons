#행렬제곱

#분할정복? logn
a, b, c = map(int,input().split())

nums = [a]
a %= c
tn = 1
num = 1

for i in range(32):
    nums.append((nums[i]*nums[i])%c)

for i in range(32, -1, -1):
    if(b >= 2**i):
        #print(b, 2**i)
        num = (num * nums[i])%c
        b-=2**i
        



print(num)
'''
그러니까, a*a*a*a*...에는 전체에 %c를 하는 것과 다를 바 없다

그러니까, (a*a)%c * (a*a)%c * ... 도 같을 것이고,

((a*a)%c * (a*a)%c) * ((a*a)%c * (a*a)%c)도 같을 것이다.

그럼 b번인 걸 줄일 수 있지...

a = a*a..처럼 제곱해서 하면

배열을 바닥부터 쌓아가기로..? 음?

'''

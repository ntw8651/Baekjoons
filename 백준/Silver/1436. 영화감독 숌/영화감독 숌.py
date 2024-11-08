N = int(input())
number = 0

while(N != 0):
    number += 1
    if('666' in str(number)):
       N-=1
#잠깐, 이러면 6이 어느부분에 666인지 알아야하는데
       #예를 들어 626이면 어... 그럼 그냥 666으로...해야하나
print(number)
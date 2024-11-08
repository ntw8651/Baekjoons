nums = [0 for i in range(10)]
n =input()
count = 0
length = len(n)
for i in range(length):
    count = int(n[i])
    tnums = [1 for j in range(10)]

    #forward 그 숫자부터 앞에 있는 값
    if(i == 0):
        forward = 0
    else:
        forward = int(n[:i])

    #backward 그 숫자부터 뒤에 있는 값
    if(i+1 == length):
        backward = 0
    else:
        backward = int(n[i+1:])

    #######################################
    
    nums[count] += backward+1 #앞의 수와 관련 없이 뒤의 수에 따른 개수
    
    for j in range(0, count): #앞의 수와 관련 없이 현재 자리에 따른 개수
        nums[j] += 10**(length-i-1)

    for j in range(0, 10): #앞의 수와 뒤에 오는 경우의 수
        nums[j] += (forward) * 10**(length-i-1)

for i in range(length): #허위값(0이 앞에 있는 경우들) 제거
    nums[0] -= 10**i

for i in nums:
    print(i, end= " ")

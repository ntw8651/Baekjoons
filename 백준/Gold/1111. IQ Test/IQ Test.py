#끝까지 남은 쌍이 정답
#b는 -100부터 100까지
#a도 -100부터 100까지
#대략 40000정도...

#에엥ㅇ에?? 이 쌍 밖이 된다고
#-100 100 이면...어엄 ㅁ모르겠고
#개억까 눈물이 주륵주륵
'''
앞 a 뒤 b 뒤뒤 c
a*x+y = b
b*x+y = c

1*3+1 = 4
4*3+1 = 13
1*3 - 4 = -1
4*3 - 13 = -1
1*3 - 4 = 4*3 - 13
(3)*3 = (-13 + 4)
5*3 = 

여기서 a와 b가 주어질 때 x와 y 찾기
식을 만드려면 최소 두개의 식 필요
a*x-b = -y
b*x-c = -y



즉 a*x-b = b*x-c
(a-b)x = b - c
x = (b - c) / (a - b)
가 된다.
그러니까 값 3개만 있으면 일단 답이 나오는거네

만약 여기서 나누어 떨어지지 않으면 구할 수 없는 경우 인거고
2개일 때에는 똑같은 게 나왔을 때만 구할 수 있겠고, 왜냐면 다른 수는
경우의 수가 무한해지니까

1개일 때에도 무한해지니까 구할 수 없겠네

오키 이대로 가보자

그리고 이걸 모든 칸에 적용시켜봐야 하네



'''
n = int(input())
nums = list(map(int ,input().split()))
results = {}

if(n == 1):
    print("A")
elif(n == 2):
    if(nums[0] == nums[1]):
        print(nums[0])
    else:
        print("A")
else:
    #아잇 그냥 등차수열인지 따로 체크할까
    #맞...지않ㅎ을까? ㅎ;
    flag = 1
    for i in range(n-1):
        if(nums[1] - nums[0] != nums[i+1] - nums[i]):
            flag = 0
    if(flag == 0):
        if((nums[0] - nums[1]) != 0):
            if((nums[1] - nums[2]) % (nums[0] - nums[1]) == 0):
                x = (nums[1] - nums[2]) // (nums[0] - nums[1])
                y = -(nums[0] * x - nums[1])
                flag = 1
                for i in range(n-1): #모든 칸에서 해당하는가?
                    if(nums[i] * x + y != nums[i+1]):
                        flag = 0
                        break
                if(flag):
                    print(nums[-1] * x + y)
                else:
                    print("B")
            else:
            #노노 구할 수 없다 -> 성립 X B
                print("B")
        else:
            #0으로 나눈다니 이무슨
            print("B")
    else:
        print(nums[-1] + nums[1] - nums[0])

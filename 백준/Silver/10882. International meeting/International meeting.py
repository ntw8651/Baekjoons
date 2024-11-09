n = int(input())
time, flag = input().split()
time = list(map(int, time.split(':')))
time = time[0]*60+time[1]

flag = float(flag[3:])

for i in range(n):
    inp =float(input()[3:])
    diff = inp - flag

    result = int(time + int(diff*60))
    result = result%(60*24)
    
    
    print("{0:0>2}:{1:0>2}".format(result//60,result%60))

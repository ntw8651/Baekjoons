n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [0 for i in range(10)]

def qwer(nowN, count, string, visit):
    string += " " + str(nums[nowN-1])
    visit[nowN] = 1
    #print(string, count)
    if(count >= m-1):
        print(string[1:])
        return
    for i in range(1, n+1):
        if(not visit[i]):
            qwer(i, count+1, string, visit.copy())
    

for i in range(1, n+1):
    qwer(i, 0, "", visit.copy())

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
g = set([])
visited = [0 for i in range(10)]

def qwer(nowN, count, string, visited):
    global g
    visited[nowN] = 1
    string += " " + str(nums[nowN-1])
    #print(string, count)
    if(count >= m-1):
        if(string not in g):
            g.add(string)
            print(string[1:])
        return
    for i in range(1, n+1):
        if(visited[i] == 0):
            qwer(i, count+1, string, visited.copy())
            
for i in range(1, n+1):
    qwer(i, 0, "", visited.copy())


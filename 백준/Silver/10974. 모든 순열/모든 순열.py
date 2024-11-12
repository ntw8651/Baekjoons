n = int(input())
visited = [0 for i in range(n)]
arg = [0 for i in range(n)]
def maker(now, visited, arg):
    if(now == n):
        string = ''
        for i in arg:
            string += str(i) + ' '
        print(string)
    for i in range(n):
        if(not visited[i]):
            arg[now] = i+1
            visited[i] = 1
            maker(now+1, visited, arg)
            visited[i] = 0
        
maker(0, visited, arg)

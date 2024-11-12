'''
토네이도 모양으로 이동하는 코드
각 방향에 따라 뿌리는 코드
'''
n = int(input())
board = []
summation = 0
for i in range(n):
    board.append(list(map(int,input().split())))
    summation+=sum(board[i])
percentL = [[0, 0, 0.02, 0, 0],
           [0, 0.1, 0.07, 0.01, 0],
           [0.05, 0, 0, 0, 0],
           [0, 0.1, 0.07, 0.01, 0],
           [0, 0, 0.02, 0, 0]]

percentR = [[0, 0, 0.02, 0, 0],
            [0, 0.01, 0.07, 0.1, 0],
            [0, 0, 0, 0, 0.05],
            [0, 0.01, 0.07, 0.1, 0],
            [0, 0, 0.02, 0, 0]]

percentU = [[0, 0, 0.05, 0, 0],
            [0, 0.1, 0, 0.1, 0],
            [0.02, 0.07, 0, 0.07, 0.02],
            [0, 0.01, 0, 0.01, 0],
            [0, 0, 0, 0, 0]]

percentD = [[0, 0, 0, 0, 0],
            [0, 0.01, 0, 0.01, 0],
            [0.02, 0.07, 0, 0.07, 0.02],
            [0, 0.1, 0, 0.1, 0],
            [0, 0, 0.05, 0, 0]]



direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
nowDirect = 0
count = 1
mCount = 1
x = n//2
y = n//2
ans = 0
while(1):
    #print(x, y)
    if(x == 0 and y == 0):
        break
    if(count == 0):
        #방향전환
        #print(x, y)
        if(nowDirect == 1 or nowDirect == 3):
            mCount+=1
        nowDirect+=1
        if(nowDirect>3):
            nowDirect = 0
        count = mCount
    else:
        #이동
        #print(nowDirect, "asdf")
        x += direct[nowDirect][0]
        y += direct[nowDirect][1]
        
        disp = 0
        if(nowDirect == 0):
            for xx in range(-2, 3):
                for yy in range(-2, 3):
                    if(x+xx < 0 or x+xx>=n or y+yy < 0 or y+yy >=n):
                        #소멸
                        ans += int(board[y][x] * percentL[yy+2][xx+2])
                        disp += int(board[y][x] * percentL[yy+2][xx+2])
                    else:
                        board[y+yy][x+xx] += int(board[y][x] * percentL[yy+2][xx+2])
                        disp += int(board[y][x] * percentL[yy+2][xx+2])


            if(x-1<0):
                ans += board[y][x] - disp
            else:
                board[y][x-1] += board[y][x] - disp

        if(nowDirect == 1):
            for xx in range(-2, 3):
                for yy in range(-2, 3):
                    if(x+xx < 0 or x+xx>=n or y+yy < 0 or y+yy >=n):
                        #소멸
                        ans += int(board[y][x] * percentD[yy+2][xx+2])
                        disp += int(board[y][x] * percentD[yy+2][xx+2])
                    else:
                        board[y+yy][x+xx] += int(board[y][x] * percentD[yy+2][xx+2])
                        disp += int(board[y][x] * percentD[yy+2][xx+2])

            if(y+1>=n):
                ans += board[y][x] - disp
            else:
                board[y+1][x] += board[y][x] - disp

        if(nowDirect == 2):
            for xx in range(-2, 3):
                for yy in range(-2, 3):
                    if(x+xx < 0 or x+xx>=n or y+yy < 0 or y+yy >=n):
                        #소멸
                        ans += int(board[y][x] * percentR[yy+2][xx+2])
                        disp += int(board[y][x] * percentR[yy+2][xx+2])
                    else:
                        board[y+yy][x+xx] += int(board[y][x] * percentR[yy+2][xx+2])
                        disp += int(board[y][x] * percentR[yy+2][xx+2])
                        
            if(x+1>=n):
                ans += board[y][x] - disp
            else:
                board[y][x+1] += board[y][x] - disp

        if(nowDirect == 3):
            for xx in range(-2, 3):
                for yy in range(-2, 3):
                    if(x+xx < 0 or x+xx>=n or y+yy < 0 or y+yy >=n):
                        #소멸
                        ans += int(board[y][x] * percentU[yy+2][xx+2])
                        disp += int(board[y][x] * percentU[yy+2][xx+2])
                    else:
                        board[y+yy][x+xx] += int(board[y][x] * percentU[yy+2][xx+2])
                        disp += int(board[y][x] * percentU[yy+2][xx+2])
            
            if(y-1<0):
                ans += board[y][x] - disp
            else:
                board[y-1][x] += board[y][x] - disp


        
        count -= 1
        board[y][x] = 0

        #for i in range(5):
            #print(board[i])
        #print("###")

print(ans)

'''
딱봐도 뭐 전체탐색이네용
5번 이동이면

4가지의 이동 겨올가 있으니까
4**5지 휴~~
마침 또 1024네~
'''
import copy
n = int(input())
boards = []
for i in range(n):
    boards.append(list(map(int,input().split())))

#0은 빈 칸
def push(direct, board, count):
    maxi = 0
    if(count == 5):
        for i in board:
            for j in i:
                if(maxi < j):
                    maxi = j
        return maxi

    if(direct == 0):
        #왼쪽으로 밀기 이게 와리가리 하다보면 멸망하는구나
        #당연히 왼쪽에 있는 것들 부터 옮겨야 함
        #비어있는 칸
        #아 합치면서 들어가야지 참
        #그러니까 미는 방향의 끝부분에서부터 pos를 내려가면서
        for i in range(n):#줄마다
            nullp = 0
            #nullp 옮기기
            #nullp가 비어있으면 넣고, 아니면 말기
            for j in range(1, n):#칸마다
                if(board[i][j] == 0):
                    continue
                while(nullp < j):
                    if(board[i][nullp] == 0):
                        board[i][nullp] = board[i][j]
                        board[i][j] = 0
                        break
                    elif(board[i][nullp] == board[i][j]):
                        board[i][nullp] *= 2
                        board[i][j] = 0
                        nullp += 1
                        break
                    else:
                        nullp += 1

    elif(direct == 2):
        for i in range(n):
            nullp = n-1
            for j in range(n-2, -1, -1):
                if(board[i][j] == 0):
                    continue
                while(nullp > j):
                    if(board[i][nullp] == 0):
                        board[i][nullp] = board[i][j]
                        board[i][j] = 0
                        break
                    elif(board[i][nullp] == board[i][j]):
                        board[i][nullp] *= 2
                        board[i][j] = 0
                        nullp -= 1
                        break
                    else:
                        nullp -= 1
    
    elif(direct == 1):#이제 위아래로, i j만 바꾸면 될듯?
        for j in range(n):
            nullp = n-1
            for i in range(n-2, -1, -1):
                if(board[i][j] == 0):
                    continue
                while(nullp > i):
                    if(board[nullp][j] == 0):
                        board[nullp][j] = board[i][j]
                        board[i][j] = 0
                        break
                    elif(board[nullp][j] == board[i][j]):
                        board[nullp][j] *= 2
                        board[i][j] = 0
                        nullp -= 1
                        break
                    else:
                        nullp -= 1

    elif(direct == 3):#이제 위아래로, i j만 바꾸면 될듯?
        for j in range(n):
            nullp = 0
            for i in range(1, n):
                if(board[i][j] == 0):
                    continue
                while(nullp < i):
                    if(board[nullp][j] == 0):
                        board[nullp][j] = board[i][j]
                        board[i][j] = 0
                        break
                    elif(board[nullp][j] == board[i][j]):
                        board[nullp][j] *= 2
                        board[i][j] = 0
                        nullp += 1
                        break
                    else:
                        nullp += 1
    #for i in board:
    #    print(i)
    #print(direct, count, "#####")

    
    for i in range(4):
        value = push(i, copy.deepcopy(board), count+1)
        if(value > maxi):
            maxi = value

    return maxi


maxi = 0
for i in range(4):
    value = push(i, copy.deepcopy(boards), 0)
    if(value > maxi):
        maxi = value
print(maxi)

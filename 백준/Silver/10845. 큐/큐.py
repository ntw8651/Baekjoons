import sys
input = sys.stdin.readline

queue = []




N = int(input())
for i in range(N):
    command = input().strip()
    if(' ' in command):
        command = command.split()
        if(command[0] == 'push'):
            queue.append(command[1])
    else:
        if(command == 'pop'):
            if(queue == []):
                print(-1)
            else:
                print(queue.pop(0))  
        elif(command == 'size'):
            print(len(queue))
        elif(command == 'empty'):
            print(int(queue == []))
        elif(command == 'front'):
            if(queue==[]):
                print(-1)
            else:
                print(queue[0])
        elif(command == 'back'):
            if(queue == [] ):
                print(-1)
            else:
                print(queue[-1])

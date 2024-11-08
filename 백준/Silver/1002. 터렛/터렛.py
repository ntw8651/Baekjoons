T = int(input())
b = []
for i in range(T):
    b.append(map(int, input().split()))
for b_list in b:
    x, y, r, x2, y2, r2 = b_list
    b_len = ((max(x,x2) - min(x, x2))**2 + (max(y,y2) - min(y, y2))**2) ** 0.5#두 점 사이의 길이
                
    if x == x2 and y == y2: # 점의 위치가 겹칠 때
        if r == r2: #and 선분의 길이가 같을 때
            print(-1)
        else:
            print(0)
            
    elif b_len == r+r2:#점과 점 사이의 거리가 주어진 거리와 합이 같을 때
        print(1)
        
    else: #점의 위치가 다를 때
        if(b_len > r+r2): # 길이가 미달일 때
            print(0)

        elif((min(r,r2) + b_len) == max(r, r2)):#긴 선분이 짧은 선분+점사이의 거리와 같을때
            print(1)
            
        elif((min(r,r2)+ b_len) < max(r,r2)): #긴 선분이 짧은 선분+점사이의 거리보다 길 
            print(0)
            
        else:
            print(2) #그 밖에는 모두 2개

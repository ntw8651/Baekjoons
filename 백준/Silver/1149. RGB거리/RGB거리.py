N = int(input())
rgb_list = []
rgb = list(map(int, input().split()))

if(N == 1):
    print(min(rgb))
else:
    rgb_list.append(rgb)
    for i in range(0, N-1):
        rgb = list(map(int, input().split()))
        b = []
        b.append(rgb[0] + min(rgb_list[i][1], rgb_list[i][2]))
        b.append(rgb[1] + min(rgb_list[i][0], rgb_list[i][2]))
        b.append(rgb[2] + min(rgb_list[i][1], rgb_list[i][0]))
        rgb_list.append(b)
    print(min(rgb_list[-1]))
        
#rgb 입력받기
#rpg1차씩 올리기
#rgb 전수에서 자기를 제외한 가장 작은거 선택하기

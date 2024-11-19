N, D = map(int, input().split())

k_list = []
num_list = []
num_list.append(D)
for i in range(N):
    a = list(map(int, input().split()))

    if(a[1] <= D and a[0] <= D and a[1] - a[0] > a[2]):
        k_list.append(a)

    
    #일단 D넘는거 거르기
        #+ 지름길이 그냥 길보다 긴거 지우기

def road(list_temp, d_temp, distance):
    global num_list
    if(D==distance):

        num_list.append(d_temp)

    
    
    elif(list_temp == []):
        num_list.append(d_temp + (D-distance))
    #음 

    else:
        for i in list_temp:
            if(d_temp + i[2] < D and distance <= i[0]):
                list_temp_t = list(list_temp)
                list_temp_t.remove(i)#아 여기서 다 지워졌는데 또 지우려면 당연히 버그나지
                if(list_temp_t != []):
                    for p in list_temp_t:
                        if(p[1] < i[0] or p[0]<distance):
                             list_temp_t.remove(p)
                road(list_temp_t, d_temp+(i[0]-distance)+i[2], i[1])
            else:
                num_list.append(d_temp + (D-distance))
            #이럴땐 뭐다? 내일 하는거다~
                
#이건 없는 부분을 건들면 에러나는 그런건데
road(k_list, 0, 0)
print(min(num_list))#또?? 아 num이게 없을수도 있지
    #지름길을 안 탈 수도 있으니 일단 거리 기본값을 D로
        #도중에 D<가 된다면 삭-제 머지 k_List는 왜 없지 ??멎ㅈ
#근데 생각해보니까 어... 어? 아니 버그났네 내머리 버그났
#넘겨줄때 불가능한 것들은 다 삭제해서 넘겨주나?
#이번에야말로.... 되어리/.//....
    
'''
4 100
0 100 98
0 50 4
50 99 10
99 100 1
'''
'''
2 100
2 99 79
4 86 10
'''

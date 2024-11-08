while(True):
    ans= input()
    if(ans == '0'):
        break

    #일단...뭐... 그냥 str로 해서 비교해볼까?
    length = len(ans)

    Pelidrome = True
    for i in range(length//2+length%2):
        if(ans[i] != ans[length-i-1]):
            Pelidrome = False
            break
    if(Pelidrome):
        print('yes')
    else:
        print('no')

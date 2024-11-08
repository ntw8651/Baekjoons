index_number = int(input())
addbool = False
c = int(1)#왼쪽
b = int(1)#오른쪽



while(index_number != 1):
    index_number += -1

    if(addbool == True):
        c+=1
        b+=-1
    else:
        c+=-1
        b+=1

        
    if(c == 0 or b == 0):
        if(addbool== True):
            addbool = False
            b=1
            
        else:
            addbool = True
            c=1


print(str(c)+'/'+str(b))

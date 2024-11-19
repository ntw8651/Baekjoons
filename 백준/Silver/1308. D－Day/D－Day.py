def yunYear(year):
    if(year % 4 == 0 and year%100 != 0 or year%400 == 0):
        return True

sY, sM, sD = map(int,input().split())
eY, eM, eD = map(int,input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]




if(sY+1000 < eY or (sY+1000 == eY and (sM < eM or (sM == eM and sD <= eD)))):
        print("gg")
else:
    Dday = 0
    for i in range(sY, eY):
        if(yunYear(i)):
            Dday+=366
        else:
            Dday+=365

    for i in range(0, sM-1):
        if(yunYear(sY) and i == 1):
            Dday -= 29
        else:
            Dday -= day[i]

    Dday -= sD

    for i in range(0, eM-1):
        if(yunYear(eY) and i == 1):
            Dday += 29
        else:
            Dday += day[i]

    Dday+= eD


    print("D-"+str(Dday))
        

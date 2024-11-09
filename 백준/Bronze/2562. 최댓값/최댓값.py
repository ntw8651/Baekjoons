now = int(0)
high = int(0)
pos = int(0)
now_pos = int(0)
for i in range(9):
    now_pos += 1
    now = int(input())
    if(now > high):
        high = now
        pos = now_pos
    
print(high)
print(pos)


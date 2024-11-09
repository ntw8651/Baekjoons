n = int(input())
for _ in range(n):
    text = input()
    score = 0
    for i in text:
        if(i == ' '):
            continue
        score+=ord(i)-ord('A')+1
    if(score==100):
        print("PERFECT LIFE")
    else:
        print(score)

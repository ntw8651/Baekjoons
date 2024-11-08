N = int(input())
cards = [i for i in range(1, N+1)]

while(len(cards)!=1):
    if(len(cards)%2==0):#짝수, 절반 씩 줄어듦
        cards = [cards[i] for i in range(1, len(cards), 2)]

    else:#홀수, 하나 씩 줄여서 다시 짝수로 만듦
        del cards[0]
        cards.append(cards.pop(0))

    

print(cards[0])



'''
      짝수면 재배치가 되는데, 홀수면 안돼
      둘을 다르게 처리해볼까?

      #일단 결국엔 원래 크기대로 배열이 되긴 하지
      #아 짝수개일 땐 한번에 반씩 줄일 수 있고,
      #홀수 개일 땐, 하나씩 줄이는 식으로 하면 되겠구나

'''

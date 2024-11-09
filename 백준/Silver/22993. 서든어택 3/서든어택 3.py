N = int(input())

inyes = True
player = list(map(int, input().split()))
b = int(player[0])
del player[0]
player.sort()
for i in range( N-1):
	if(player[i] <b):
		b+=player[i]
	else:
			inyes = False
			break
if(inyes):
			print("Yes")
else:
			print("No")
			
	
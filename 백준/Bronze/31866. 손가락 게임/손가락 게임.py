a, b = map(int,input().split())

if(a == 2 and b == 5):
    print('>')
elif(b == 2 and a == 5):
    print('<')
    
elif(a == 0 and b == 5):
    print('<')
elif(b == 0 and a == 5):
    print('>')

elif(a == 2 and b == 5):
    print('>')
elif(a == 5 and b == 2):
    print('<')

elif(a==2 and b == 0):
    print('<')
elif(a==0 and b==2):
    print('>')

elif(((a == 2)or(a == 5)or(a == 0)) and ((b != 2) or (b != 5) or (b != 0)) and a!=b):
    print('>')
elif(((b == 2)or(b == 5)or(b == 0)) and ((a != 2) or (a != 5) or (a != 0)) and a!=b):
     print('<')
else:
    print('=')

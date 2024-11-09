'''
1면으로 최소 : 면
2면으로 최소 : 선
3면으로 최소 : 꼭짓점

n은 1일때는 예외처리
'''
n = int(input())
a, b, c, d, e, f = map(int, input().split())
aa = [a,b,c,d,e,f]
bb = [a+d, a+b, a+c, a+e, b+d, b+c, e+d, e+c, f+d, f+b, f+c, f+e]
cc = [a+b+d, a+b+c,a+c+e,a+e+d,f+b+d, f+d+e, f+e+c, f+c+b]

if(n == 1):
    print(sum(aa) - max(aa))
else:
    ans = 0
    if(n>2):
        #면
        ans += (n-2)**2 * 5 * min(aa)
        ans += (n-2) * 4 * min(aa)
    if(n>1):
        #선
        ans += (n-1) * 4 * min(bb)
        ans += (n-2) * 4 * min(bb)
    #점
    ans+= 4 * min(cc)
    print(ans)

'''
들어가는 개수와 어디로 향할 수 있는 지만 저장하기
만약 들어가는 개수가 0이다? 걘 루트로 두고 출력하고 find시작
만약 들어가는 개수가 1이다? 걘 출력해주고 다음으로 향하기
만약 들어가는 개수가 2이상이다? 걘 출력ㄴㄴ 개수 1줄이고 백트래킹

진짜 완-벽하다
'''
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int,input().split())
nums = [[0,[]]]+[[0, []] for i in range(n)]
for i in range(m):
    s, e = map(int, input().split())
    nums[s][1].append(e)
    nums[e][0] += 1

def find(now, nums):
    if(nums[now][0] == 1):
        print(now, end = " ")
    elif(nums[now][0] > 1):
        nums[now][0] -= 1
        return 0
    for i in nums[now][1]:
        find(i, nums)

for i in range(1, n+1):
    if(nums[i][0] == 0):
        print(i, end = " ")
        find(i, nums)

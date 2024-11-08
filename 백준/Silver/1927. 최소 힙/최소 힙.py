import heapq as hq
import sys
input = sys.stdin.readline
heap = []

hq.heapify(heap)
n = int(input())
for i in range(n):
    inp = int(input())
    if(inp):
        hq.heappush(heap, inp)
    else:#inp == 0
        if(len(heap) == 0):
            print(0)
        else:
            print(hq.heappop(heap))

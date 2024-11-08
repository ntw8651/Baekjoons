import sys
words = set()
n = int(input())
for i in range(n):
    words.add(input())

words = sorted(list(words), key = lambda x : (len(x), x))
for i in words:
    print(i)

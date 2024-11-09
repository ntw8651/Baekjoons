n = int(input())
for i in range(n):
    left, right = input().split()
    print("Distances: ", end = "")
    for k in range(len(left)):
        val = ord(right[k]) - ord(left[k])
        if(val < 0):
            val+=26
        print(val, end = " ")
    print()

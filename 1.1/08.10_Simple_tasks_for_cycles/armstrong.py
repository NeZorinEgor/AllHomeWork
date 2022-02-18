N = int(input())
for x in range (1, N + 1):
    tmp = 0
    for i in str(x):
        tmp += int(i) ** len(str(x))
        if tmp == x:
            print(x)

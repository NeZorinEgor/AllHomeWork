li = [10, 15, 81, 9, 11, 27, 55, 441, 28]
n = len(li)
for j in range(0,n-1):
    for i in range(0,n-j-1):
        if li[i] < li[i+1]:
            li[i],li[i + 1] = li[i + 1], li[i]
            print(li)

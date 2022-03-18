a = input().split()
c = map(int,a)
b = 0
for i in list(c):
    if i % 3 == 0:
        b += 1
print(b)

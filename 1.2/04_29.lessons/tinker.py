file = open("tinker.txt")
i = 1
l = 0
for line in file:
    if i in range

    i += len(line.strip('\n'))
    

print("i:", i)

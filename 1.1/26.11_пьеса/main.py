nomer = 0
d = { }
replici = []
roles = []


with open("roles.txt", "r",encoding='utf-8') as file:
    for line in file:
        line = line.rstrip()
        if line != "roles:":
            if line != "textLines:":
                roles.append(line)
            else:
                break



    roles.append("Слова автора")
    roles.sort()


    for i in range(len(roles)):
        replici.append([])
    for line in file:
        nomer += 1
        line = line.rstrip()
        if ":" in line:
            if "(" in line:
                value = line.partition("(")[2]
                for i in range(len(roles)):
                    if "Слова автора" == roles[i]:
                        replici[i].append(value.replace(')', ''))
                line = line.partition("(")[0]



            if line.partition(":")[0] in roles:
                key = line.partition(":")[0]
                value = line.partition(":")[2]
                d[key] = value
                for i in range(len(roles)):
                    if key == roles[i]:
                        result = str(nomer) + str(")") + str(d[key])
                        replici[i].append(result)
                last_key = key



        else:
            if "(" in line:
                value = line.partition("(")[2]
                for i in range(len(roles)):
                    if "Слова автора" == roles[i]:
                        replici[i].append(value.replace(')', ''))



            else:
                value = line
                d[last_key] = value
                for i in range(len(roles)):
                    if last_key == roles[i]:
                        replici[i].append(d[last_key])


for i in range(len(roles)):
    print(str(roles[i]) + str(": "))
    for j in range(len(replici[i])):
        print(replici[i][j])
    print()
print(replici)
print(roles)

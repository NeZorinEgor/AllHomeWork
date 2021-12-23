def file():
    import random
    file=open("nums.txt","w")
    a=[x for x in range(300)]
    random.shuffle(a)
    for l in a:
        file.write(str(l))
        file.write("\n") 
    
print("Зорин Егор 14124 Программа сортирует созданный файл при помощи метода: быстрая сортировка")
 
while True:
        offer=input("Создать файл sortirovka.txt с случайными числами от 0 до 300? [Да\Нет] ")
        if offer=="Да":
            file()
            break
        elif offer=="Нет":
            print
            break
        print("\n")
 
 
with open('nums.txt') as f:
    text = [int(x) for x in f]
    
import random
 
def sort(text):
    if len(text) <= 1:
        return text
    else:
        q = random.choice(text)
        L = [elem for elem in text if elem < q]
        M = [q] * text.count(q)
        R = [elem for elem in text if elem > q] 
        return sort(L) + M + sort(R)
print(sort(text))

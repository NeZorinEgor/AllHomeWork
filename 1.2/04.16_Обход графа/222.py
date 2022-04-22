#flines = open('msm.txt').readlines()
#ms = {i[0]: {flines[0].split()[1:][j]: int(i.split()[1:][j]) for j in range(len(i.split()[1:]))} for i in flines[1:]}
import sys
import math as m
visited=[]
dist={}
pred={}

s =("Добро пожаловать в мою программу, которая поможет найти вам минимальный путь в графе! Вводить можно только вершины графа от A до Н заглавными англисскими буквами!!! Так же вы в любой момент можете остановить программу, если напишите 'stop'.")
print(s)


def sp(g,go,ta,visited=[],dist={},pred={}):
    if not visited:
        dist[go]=0
    if go==ta:
        path=[]
        while ta != None:
            path.append(ta)
            ta=pred.get(ta,None)
        return dist[go], path[::-1]
    for n in g[go]:
        if n not in visited:
            neigh = dist.get(n,sys.maxsize)
            ten = dist[go] + g[go][n]
            if ten< neigh:
                dist[n] = ten
                pred[n]=go
    visited.append(go)
    unv = dict((k, dist.get(k,sys.maxsize)) for k in g if k not in visited)
#Эта функция возвращает целое число, которое обозначает, какое максимально значение может иметь переменная типа Py_ssize_t
    ct = min(unv, key=unv.get)
#Метод get() возвращает значение для данного ключа. Если ключ недоступен, возвращается значение по умолчанию None.
    return sp(g,ct,ta,visited,dist,pred)

if __name__ == "__main__":
    flines = open('msm.txt').readlines()
    g = {i[0]: {flines[0].split()[1:][j]: int(i.split()[1:][j]) for j in range(len(i.split()[1:]))} for i in flines[1:]}

while True:
    
    try:
        go = input("Начальная точка: ")
        if go == 'stop':
            print("Программа остановлена")
            break
        ta = input("Конечная точка: ")
        print ("Минимальный путь:", sp((g),go,ta,visited=[],dist={},pred={}))
    except (KeyError, ValueError):
        print("Неправильно выполнен ввод =( Введите корректные значени!")

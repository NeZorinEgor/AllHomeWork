a = []
o = int(input('Введите номер островков, которые хотите подсчитать от 1 до 9:'))
if o>=1 and o<=9:
    with open('txt.txt') as f:
        for line in f:
            a.append(list(map(int, line.rstrip())))
            
    print(a)
    ep = 10
    

    def search_group(ar, row, elem):
        if ar[row][elem] == o:
            ar[row][elem] = ep
            if elem < len(ar[row]) - 1:
                search_group(ar, row, elem + 1)
            if row < len(ar) - 1:
                search_group(ar, row + 1, elem)
            if elem > 0:
                search_group(ar, row, elem - 1)
            if row > 0:
                search_group(ar, row - 1, elem)
        else:
            return

    rec_a = [i.copy() for i in a]
    gr_cntr = 0
    for row in range(len(rec_a)):
        for elem in range(len(rec_a[row])):
            if rec_a[row][elem] == o:
                gr_cntr = gr_cntr + 1
                search_group(rec_a, row, elem)
                
    print("Количестсво островrов:", gr_cntr)
else:
     print('Вы ввели некоректное значение')


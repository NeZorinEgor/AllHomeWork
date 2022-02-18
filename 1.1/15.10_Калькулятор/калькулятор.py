while True:
    s = input("Введите оператор (+, -, *, / или stop (стоп) для остановки программы): ")
    if s == 'stop' or s == 'стоп':
        print("Программа остановлена")
        break
    if s in ('+', '-', '*', '/'):
        while True:
            try:
                n1 = int(input("Введите первое число = "))
                n2 = int(input("Введите второе число = "))
                break
            except ValueError:
                print("Программа работает только с числами!")
        if s == '+':
            print("Oтвет:",('{} + {} ='.format(n1, n2)),(n1+n2))
        elif s == '-':
            print("Oтвет:",('{} - {} ='.format(n1, n2)),(n1-n2))
        elif s == '*':
            print("Oтвет:",('{} * {} ='.format(n1, n2)),(n1*n2))
        elif s == '/':
            if n2 != 0:
                print("Oтвет:",('{} / {} ='.format(n1, n2)),(n1/n2))
            else:
                print("Деление на ноль нельзя!")
    else:
        print("Вы ввели неправильный оператор! Повторите попытку.")

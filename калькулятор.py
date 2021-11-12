n = input("Операция( + - * /): ")
a = float(input('a = '))
b = float(input('b = '))
e = "Оба значения должны быть числами!"
if n == '+':
    print(a + b)
elif n == '-':
    print(a - b)
elif n == '*':
    print(a * b)
elif n == '/':
    if b != 0:
        print(a / b)
    else:
        print("Делить на ноль нельзя!")

import math
print("|:___Введите базовую математическую операцию (+,-,*,/),или другие___:|")
print("(Округление,Модуль,Корень,Степень,Факториал,Синус,Косинус,Тангенс,Котангенс)")
print("|__Продолжайте,пока это необходимо__|")
print("")
print("|----Чтобы посмотреть историю операций,введите слово <История>----|")
c=[]
while True:
    op=input()
    if op=="+":
        print("Введите 1-е число")
        a=int(input())
        print("Введите 2-е число")
        b=int(input())
        print(a+b)
        c.append(f"{a}+{b}={a+b}")
    if op=="-":
        print("Введите 1-е число")
        a=int(input())
        print("Введите 2-е число")
        b=int(input())
        print(a-b)
        c.append(f"{a}-{b}={a-b}")
    if op=="*":
        print("Введите 1-е число")
        a=int(input())
        print("Введите 2-е число")
        b=int(input())
        print(a*b)
        c.append(f"{a}*{b}={a*b}")
    if op=="/":
        print("Введите 1-е число")
        a=int(input())
        print("Введите 2-е число")
        b=int(input())
        print(a/b)
        c.append(f"{a}/{b}={a/b}")
    if op=="Округление":
        print("Введите число")
        a=float(input())
        print("Округление вниз или вверх?")
        v=input()
        if v=="вниз" or v=="Вниз":
            print(math.floor(a))
            c.append(f"Округление вниз числа {a}={math.floor(a)}")
        else:
            print(math.ceil(a))
            c.append(f"Округление вверх числа {a}={math.ceil(a)}")
    if op=="Модуль":
        print("Введите число")
        a=float(input())
        print(abs(a))
        c.append(f"Модуль числа {a}:{abs(a)}")
    if op=="Корень":
        print("Введите число")
        a=float(input())
        print(math.sqrt(a))
        c.append(f"Квадратный корень числа{a}={math.sqrt(a)}")
    if op=="Степень":
        print("Введите 1-е число(Число,которое будет возводиться)")
        a=int(input())
        print("Введите 2-е число(Степень)")
        b=int(input())
        print(math.pow(a,b))
        c.append(f"{a} в степени {b}={math.pow(a,b)}")
    if op=="Факториал":
        print("Введите число")
        a=int(input())
        print(math.factorial(a))
        c.append(f"Факториал числа {a}={math.factorial(a)}")
    if op=="Синус":
        print("Введите число(в радианах)")
        a=int(input())
        print(math.sin(a))
        c.append(f"Синус числа {a}={math.sin(a)}")
    if op=="Косинус":
        print("Введите число(в радианах)")
        a=int(input())
        print(math.cos(a))
        c.append(f"Косинус числа {a}={math.cos(a)}")
    if op=="Тангенс":
        print("Введите число(в радианах)")
        a=int(input())
        print(math.tan(a))
        c.append(f"Тангенс числа {a}={math.tan(a)}")
    if op=="Котангенс":
        print("Введите число(в радианах)")
        a=int(input())
        print(math.atan(a))
        c.append(f"Котангенс числа {a}={math.atan(a)}")
    if op=="История" or op=="история":
        print(f"Ваша история запросов:",*c,sep="\n")
        print("Хотите продолжить?")
        n=input()
        if n=="Нет" or n=="No" or n=="нет" or n=="no":
            break


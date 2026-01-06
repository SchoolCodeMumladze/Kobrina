import math
c=[]
while True:
    op=input()
    if op=="+":
        a=int(input())
        b=int(input())
        print(a+b)
        c.append(f"{a}+{b}={a+b}")
    if op=="-":
        a=int(input())
        b=int(input())
        print(a-b)
        c.append(f"{a}-{b}={a-b}")
    if op=="*":
        a=int(input())
        b=int(input())
        print(a*b)
        c.append(f"{a}*{b}={a*b}")
    if op=="/":
        a=int(input())
        b=int(input())
        print(a/b)
        c.append(f"{a}/{b}={a/b}")
    if op=="Округли":
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
        a=float(input())
        print(abs(a))
        c.append(f"Модуль числа {a}:{abs(a)}")
    if op=="Корень":
        a=float(input())
        print(math.sqrt(a))
        c.append(f"Квадратный корень числа{a}={math.sqrt(a)}")
    if op=="Степень":
        a=int(input())
        b=int(input())
        print(math.pow(a,b))
        c.append(f"{a} в степени {b}={math.pow(a,b)}")
    if op=="Факториал":
        a=int(input())
        print(math.factorial(a))
        c.append(f"Факториал числа {a}={math.factorial(a)}")
    if op=="История" or op=="история":
        print(f"Ваша история запросов:{c}")
        print("Хотите продолжить?")
        n=input()
        if n=="Нет" or n=="No" or n=="нет" or n=="no":
            break


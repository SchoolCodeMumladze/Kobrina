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
    if op=="История":
        print(f"Ваша история запросов:{c}")
        print("Хотите продолжить?")
        n=input()
        if n=="Нет" or n=="No":
            break


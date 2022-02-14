def modular(a,b):
    d=int(a/b)
    c=(a-d*b)
    return c

x = int(input("enter divident"))
y = int(input("enter divisor"))
print(modular(x,y))

from math import sqrt
print("giải phương trình bậc 2:a*x^2+b*x+c")
a=float(input("nhập a: "))
b=float(input("nhâp b: "))
c=float(input("nhập c: "))
if a==0:
    if b==0:
        if c==0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        if c==0:
            print("phương trình có 1 nghiêm x = 0")
        else:
            print("phương trình có 1 nghiễm= "-c/b)
else:
    delta = b*b-4*a*c
    if delta == 0:
        print("phương trình có nghiệm kép x= ",-b/(2*a))
    else:
        print("phương trình có hai mnhghieejm phân biệt")
        print("x1= ",float((-b-sqrt(delta))/(2*a)))
        print("x2= ", float((-b)+sqrt(delta))/(2*a))

def benefit(t,n,k):
    return t/100*n*k
t=int(input("nhập t: "))
n=int(input("nhập n: "))
k=int(input("nhập k: "))
print(t/100,"*",n,"*",k,"=",benefit(t,n,k))

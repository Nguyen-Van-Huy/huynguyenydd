pi=3.14
R=input("Bán kính: ")
def cv(R,pi):
    return 2*pi*R
def dt(R,pi):
    return sqr(R)*pi
print("1.cv")
print("2.dt")
choice=input("Enter choice(1/2):")
if choice=='1':
    print(2,"*",pi,"*",R,"=",cv(R,pi))
elif choice=='2':
    print(sqr(R),"*",pi)
else:
    print("Invalid input")

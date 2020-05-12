class Circle(object):
    def __init__(self, r):
        self.r = r
    def dt(self):
        return self.r**2*3.14
    def cv(self):
        return self.r*2*3.14
r=int(input("Nhập r: "))
a=Circle(r)
print(a.dt())
print(a.cv())

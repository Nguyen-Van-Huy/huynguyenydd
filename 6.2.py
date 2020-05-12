class Hcn(object):
    def __init__(self, d, r):
        self.d = d
        self.r = r
    def area(self):
        return self.d*self.r
d=int(input (" nhập d: "))
r=int(input (" nhap r: "))

a=Hcn(d,r)
print(a.area())

def mymath:
def square(n):
    return n*n
def cube(n):
    return n*n*n
def average(values):
    nvals=len(values)
    sum=0.0
    for v in values:
        sum += v
    return float(sum)/nvals
import mymath.py
values = [2,4,6,8,10]
print('Squares: ')
for v in values:
    print(mymath.square(v))
print ('cubes:')
for v in values:
    print(mymath.cube(v))
    print('Average: ' +str(mymath.average(values)))
import mymath as mt
print(mt.square(2))
print(mt.square(3))
    

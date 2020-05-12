import numpy as np

a = np.array([1, 2, 3]) # Tạo một numpy array với rank = 1

print(type(a))            # Sẽ in ra "<class 'numpy.ndarray'>"
print(a.shape)            # Sẽ in ra "(3,)"
print(a[0], a[1], a[2])   # Sẽ in ra "1 2 3"
a[0] = 5                  # Thay đổi giá trị của 1 phần tử trong mảng
print(a)                  # Sẽ in ra kết quả là "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Tạo một numpy array với rank =2
print(b.shape)                     # In ra "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Sẽ in ra "1 2 4"

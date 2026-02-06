import numpy as np

a = np.array([2, 3, 4])
print(a)
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(c.shape)
print(c.dtype)

zeros = np.zeros((3, 4))
ones = np.ones((2, 3), dtype=np.int16)
empty = np.empty((2, 4))

np.arange(10, 30, 5)
np.linspace(0, 2, 9)

from numpy import  pi
x = np.linspace(0,2 *pi, 100)
y = np.sin(x)

a = np.array([20, 30, 40, 50])
b = np.arange(4)

a - b
b ** 2
10 * np.sin(a)

A = np.array ([[1,1], [0,1]])
B = np.array ([[2,0], [3,4]])
A * B
A @ B

b = np.arange(12).reshape(3,4)
print(b)

b.sum(axis=0)
b.min(axis=1)
b.cumsum(axis=1)

a = np.arange(10) ** 3
a[2]
a[2:5]
a[:6:2]
a[::-1]
a[a > 100]

def f(x, y):
    return 10 * x +y

b = np.fromfunction(f, (5,4), dtype =int)
b[:,1]
b[1:3,:]
a = np.floor(10 * np.random.random((3,4)))
a.shape
a.ravel()
a.reshape(6,2)

a.T
np.vstack((a, a))
np.hstack((a, a))
np.hsplit(a, 2)

sensor = np.array([
    [21.5, 22.1, 21.9],
    [20.9, 21.3, 21.0],
    [22.4, 22.8, 23.0]
])

data = np.random.randint(0, 100, size = (10,5))


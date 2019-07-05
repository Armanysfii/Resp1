import numpy as np

a = np.array(np.arange(24)).reshape(2, 3,4)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(type(a))
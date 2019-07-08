import numpy as np

a = np.array(np.arange(24)).reshape(2, 3, 4)
b = np.append(a, [1, 2, 3, 4])
print(a)
print(b)
b.reshape(7, 4)
print(b)


c = np.array(np.arange(24)).reshape(2, 3, 4) * 10 + 3
print(c)

print(np.append(a,c, axis=0))
print(np.append(a,c, axis=0).shape)

after_insert_c = np.insert(c, 1, 444, axis=1)

d = np.array(np.arange(20)).reshape(2, 4, 2)
np.delete(d, 1, axis=1)
print(d)
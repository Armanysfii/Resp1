import numpy as np

### linspace
mLinspace = np.linspace(5, 15, 9, retstep=True)
print(mLinspace)
print(mLinspace[1])

### zeros
print(np.zeros(5, dtype='int64')) # type casting with dtype attribute
print(np.zeros((5, 5))) # multi dimensional array

### ones
print(np.ones(7, dtype='int64'))
print(np.ones((8, 8)))

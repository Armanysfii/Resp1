import numpy as np

print(np.__version__)

# list array
mlist = [1, 1, 12, 23, 4, 6, 90]
mmlist = np.array(mlist)
print(mmlist * 10)

# tuples
mTuple = (14, -3, 23, 5+2j)
print(np.array(mTuple))

# difference between python and numpy data structures
print(mTuple * 6)           # replicates six times
print(np.array(mTuple)*6)   # each index multiplies  to six


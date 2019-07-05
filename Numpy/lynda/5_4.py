import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
together = np.concatenate((a, b))
print(a, "\n\n",
      b, "\n\n",
      together)

# stacks
# stack0 = np.stack(a, axis=0)
# stack1 = np.stack(a, axis=1)
# stack2 = np.stack(a, axis=2)


# split
a_split = np.arange(5)
print(np.split(a_split, 1))
print(a_split[1], "\n", a_split[1].shape)


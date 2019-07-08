import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 3 *np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.plot(x, y1)
# plt.plot(x, y2)
# or
plt.plot(x, y1, "r--", x, y2, "y:")

plt.legend(["sin", "cos"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine")
plt.show()
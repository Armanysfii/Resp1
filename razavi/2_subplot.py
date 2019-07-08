import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1.4, 1.4, 30)
plt.subplot(2,2,1)
plt.plot(x, x)
plt.subplot(2,2,2)
plt.plot(x, x**2)
plt.subplot(2,2,3)
plt.plot(x, x**3)
plt.subplot(2,2,4)
plt.plot(x, x**4)
plt.show()


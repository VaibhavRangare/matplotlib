import matplotlib.pyplot as plt
import numpy as np


# x = np.linspace(0, 10)
x = [0, 90, 180, 270, 360]
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.xticks([0, 90, 180, 270, 360])
plt.yticks([1, 2, 3, 4, 5])
plt.grid()
plt.show()

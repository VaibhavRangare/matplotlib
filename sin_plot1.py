import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10)
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.grid()
plt.show()

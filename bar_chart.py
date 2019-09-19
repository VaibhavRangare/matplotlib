import matplotlib.pyplot as plt
import numpy as np


x = np.arange(2012, 2015)
y = [2, 5, 9]
plt.figure()
plt.grid()
plt.bar(x, y)
plt.show()

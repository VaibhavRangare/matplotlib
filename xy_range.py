import matplotlib.pyplot as plt


x = [0, 90, 180, 270, 360]
y = [2, 3, 2, 1, 0]
plt.figure()
plt.plot(x, y)
plt.xticks([0, 90, 180, 270, 360])
plt.yticks([1, 2, 3, 4, 5])
plt.grid()
plt.show()

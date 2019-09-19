import matplotlib.pyplot as plt


x = [0, 90, 180, 270, 360]
y = [2, 3, 2, 1, 0]
y1 = [0, 1, 3, 2, 1]
plt.figure()
plt.plot(x, y, label="Python")
plt.plot(x, y1, label="R", marker='*', color='gray')
plt.xticks([0, 90, 180, 270, 360])
plt.yticks([1, 2, 3, 4, 5])
plt.xlabel('Angle')
plt.ylabel('Values')
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt


x = [0, 90, 180, 270, 360]
y = [2, 3, 2, 1, 0]
y1 = [0, 1, 3, 2, 1]
plt.figure()
plt.xticks([0, 90, 180, 270, 360])
plt.yticks([1, 2, 3, 4, 5])
plt.xlabel('Angle')
plt.ylabel('Values')
plt.legend()
plt.scatter(x, y)
plt.show()

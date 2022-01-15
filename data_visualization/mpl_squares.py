import matplotlib.pyplot as plt


imput_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(imput_values, squares, linewidth=5)

plt.scatter(2, 4, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()

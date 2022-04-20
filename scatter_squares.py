import matplotlib.pyplot as plt

x_values = [x for x in range(1,1001)]
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fix, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqare of Value", fontsize=14)

# Set the Range of each axis
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis="both", which='major', labelsize=14)

# Display graph
plt.show()
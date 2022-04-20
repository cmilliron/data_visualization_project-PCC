import matplotlib.pyplot as plt
from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def _get_step(self):
        x_direction = choice([-1, 1])
        x_distance = choice([1, 2, 3, 4, 5])
        step = x_direction * x_distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches teh desired length. 
        while len(self.x_values) < (self.num_points):

            # Decide which direction to go and how far to go in that direction
            
            x_step = self._get_step()
            y_step = self._get_step()
            
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue 

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


"""
# Make a random walk
rw = RandomWalk() 
rw_1 = RandomWalk()
rw_2 = RandomWalk() 
rw_3 = RandomWalk()
rw.fill_walk()
rw_1.fill_walk()
rw_2.fill_walk()
rw_3.fill_walk()


# Plot the points in the walk. 
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c='red', s=15)
ax.scatter(rw_1.x_values, rw_1.y_values, c='blue', s=15)
ax.scatter(rw_2.x_values, rw_2.y_values, c='green', s=15)
ax.scatter(rw_3.x_values, rw_3.y_values, c='yellow', s=15)
"""

# Keep makin new walks, as long as the program is active. 
#while True:
# Make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use("classic")
fix, ax = plt.subplots(figsize=(15, 9), dpi=100)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)

# Emphasize the first and lsat points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Display graph.
plt.show()

"""
keep_running = input("Make another walk? (y/n): ")
if keep_running == 'n':
    break
"""
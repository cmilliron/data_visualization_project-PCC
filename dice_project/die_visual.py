from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline


# Create a 6 sided die
die = Die(8)
die_2 = Die(8)
rolls = 50000

# Make some rolls, and store results in a list
results = []
for roll_num in range(rolls):
    result = die.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die.num_sides + die_2.num_sides
for i in range(2, max_results + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

# Visualize the results. 
x_values = list(range(2, max_results + 1))
data  = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': "Frequency of Results"}
my_layout = Layout(title=f"Results of rolling a D{die.num_sides} and a D{die_2.num_sides} {rolls} times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_2.html')

print(frequencies)

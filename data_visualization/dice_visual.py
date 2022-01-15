import pygal


from die import Die


# Creating cube D6
die_1 = Die()
die_2 = Die()

# Simulation of a series of throws with saving the results to the list.
results = []

for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 5000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

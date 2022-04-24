import csv
import matplotlib.pyplot as plt
from datetime import date, datetime

filename = "data/sitka_weather_2018_simple.csv"

# Read highs from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    dates, high_temps, low_temps = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        high_temps.append(high)
        low_temps.append(low)


# Plot high temps
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, high_temps, c="red", alpha=.5)
ax.plot(dates, low_temps, c='blue', alpha=.5)
ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)

# Format plots.
ax.set_title("Daily High Temperatures, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(axis="both", which='major', labelsize=16)

# Display Plot
plt.show()
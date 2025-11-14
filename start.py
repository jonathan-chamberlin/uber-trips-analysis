import pandas as pd

trips = pd.read_csv(r"C:\Repositories for Git\uber-trips-analysis-folder\uber-raw-data-sep14.csv")

row_10 = trips.iloc[9]
print(row_10)

for n in range(1,10,1):
    print(trips.iloc[n])


#Problem 1: find busiest date

trips_by_day = trips.groupby('Date/Time')

trips['Date'] = trips['Date/Time'].apply(lambda n: n.split(' ')[0])
    # Builds a column to the trips table

busiest_date = trips['Date'].value_counts().idxmax()
most_trips_in_one_day = trips['Date'].value_counts().iloc[0]

busiest_day_message = f"The busiest date was {busiest_date}. It had {most_trips_in_one_day} trips."

print(busiest_day_message)

# Problem 2: Find time with lowest number of rides
least_busy_date = trips['Date'].value_counts().idxmin()
least_trips_in_one_day = trips['Date'].value_counts().min()

least_busy_date_message = f"The least date was {least_busy_date}. It had {least_trips_in_one_day} trips."

print(least_busy_date_message)

# Problem 3: Find Busiest hours of the day
# LEFT OFF

# Problem 4: Find Slowest hours of the day

# Problem 5: Find Most popular pickup areas (cluster Lat/Lon coordinates)

# Problem 6: Find Standard deviation of trip frequency (consistency)

# Problem 7: Identify trends over the month (increasing/decreasing demand) by creating a bar chart which shows trip volume each day.

# Problem 8: Create Heatmap of trips by hour and day of week, where the x axis is days of the week and the y axis is hour of the day, and there are cells with the cumulative total of trips taken that weekday and within that hour. Then color the cells based on value, where the lowest are red, average are white, and darkest are green.

# Problem 9: Create Scatter plot of all pickup locations (shows city shape)








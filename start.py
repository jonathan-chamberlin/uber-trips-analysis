import pandas as pd

trips = pd.read_csv(r"C:\Repositories for Git\uber-trips-analysis-folder\uber-raw-data-sep14.csv")


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

# Problem 3: Find Busiest time of the day
trips['Time'] = trips['Date/Time'].apply(lambda n: n.split(' ')[1])
#build column 'Time' as the time of the trip 

busiest_minute = trips['Time'].value_counts().idxmax()
trips_during_busiest_minute = trips['Time'].value_counts().iloc[0]

busiest_minute_message = f"The busiest minute was {busiest_minute}. Across the dataset, there were {trips_during_busiest_minute} that time."

print(busiest_minute_message)

# Problem 4: Find Slowest time of the day
least_busy_minute = trips['Time'].value_counts().idxmin()
trips_during_least_busy_minute = trips['Time'].value_counts().min()

least_busy_minute_message = f"The least busy minute was {least_busy_minute}. Across the dataset, there were {trips_during_least_busy_minute} that time."

print(least_busy_minute_message)

# Problem 5: Find Most popular pickup areas (cluster Lat/Lon coordinates)

# Problem 6: Find Standard deviation of trip frequency (consistency)

# Problem 7: Identify trends over the month (increasing/decreasing demand) by creating a bar chart which shows trip volume each day.

# Problem 8: Create Heatmap of trips by hour and day of week, where the x axis is days of the week and the y axis is hour of the day, and there are cells with the cumulative total of trips taken that weekday and within that hour. Then color the cells based on value, where the lowest are red, average are white, and darkest are green.

# Problem 9: Create Scatter plot of all pickup locations (shows city shape)








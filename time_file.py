import pandas as pd

trips = pd.read_csv(r"C:\Repositories for Git\uber-trips-analysis-folder\uber-raw-data-sep14.csv")


#Problem 1: find busiest date

trips_by_date_time = trips.groupby('Date/Time')

'''I used this to check my understanding of the .split() function
te = "09/03/2024".split("/"), and ultimately to create date_format
print(te)
print(te[0])
print(te[1])
print(te[2])'''

def date_format(date: str) -> str:
    '''Takes a date in the format of M/D/YYYY, and converts it into YYYY/MM/DD. It makes it so if the month or day are a single digit, you add a zero before them'''
    
    split_date = date.split("/")
    month = split_date[0]
    day = split_date[1]
    year = split_date[2]
    
    if len(month) == 1:
        month = f"0{month}"
    if len(day) == 1:
        day = f"0{day}"
    
    formatted_date = f"{year}/{month}/{day}"
    
    return formatted_date


trips['Date'] = trips['Date/Time'].apply(lambda n: date_format(n.split(' ')[0]))
    # Builds a column to the trips table. From the Date/Time column, first it grabs the date, then uses formatted_date to put the date into a consistent format. Assumes all years are 4 digits.

busiest_date = trips['Date'].value_counts().idxmax()
busiest_date_value = trips['Date'].value_counts().iloc[0]

busiest_day_message = f"The busiest date was {busiest_date}. It had {busiest_date_value} trips."

print(busiest_day_message)

# Problem 2: Find time with lowest number of rides
least_busy_date = trips['Date'].value_counts().idxmin()
least_busy_date_value = trips['Date'].value_counts().min()

least_busy_date_message = f"The least date was {least_busy_date}. It had {least_busy_date_value} trips."

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

# Problem 5: Find busiest hour

trips['Hour'] = trips['Time'].apply(lambda n: n.split(':')[0])

'''Test to verify that I created the Hour column correctly
for n in range(1,100,1):
    message = f"Time is {trips.iloc[n]['Time']}, and hour is {trips.iloc[n]['Hour']}"
    print(message)
'''

busiest_hour = trips['Hour'].value_counts().idxmax()
busiest_hour_value = trips['Hour'].value_counts().max()

busiest_hour_message = f"The busiest hour of the day was {busiest_hour}, and {busiest_hour_value} trips happened that hour."
print(busiest_hour_message)

# Problem 6: Find least busy hour

least_busy_hour = trips['Hour'].value_counts().idxmin()
least_busy_hour_value = trips['Hour'].value_counts().min()

least_busy_hour_message = f"The least busy hour of the day was {least_busy_hour}, and {least_busy_hour_value} trips happened that hour."

print(least_busy_hour_message)

# Problem 7: Find Standard deviation of trip frequency (consistency)

trips_per_day = trips['Date'].value_counts().sort_index()
mean_trips_per_day = trips_per_day.mean()
median_trips_per_day = trips_per_day.median()
std_dev_of_trip_per_day = trips_per_day.std() 

std_dev_of_trip_per_day = trips_per_day.std()
# max: busiest_date_value
# min: least_busy_date_value

overall_stats_message = f"Mean trips per day: {mean_trips_per_day}\nMedian Trips per Day: {median_trips_per_day}\nStandard Deviation of Trips per Day: {std_dev_of_trip_per_day:.2f}\nMost Trips in One Day: {busiest_date_value}\nFewest Trips in One Day: {least_busy_date_value}"

print(overall_stats_message)

# Problem 8: Identify trends over the month (increasing/decreasing demand) by creating a bar chart which shows trip volume each day.

# Problem 9: Create Heatmap of trips by hour and day of week, where the x axis is days of the week and the y axis is hour of the day, and there are cells with the cumulative total of trips taken that weekday and within that hour. Then color the cells based on value, where the lowest are red, average are white, and darkest are green.










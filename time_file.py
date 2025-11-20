import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

trips['Time'] = trips['Date/Time'].apply(lambda n: n.split(' ')[1])
#build column 'Time' as the time of the trip 

trips['Hour'] = trips['Time'].apply(lambda n: n.split(':')[0])




"""THE FOLLOWING CODE WAS COMMENTED OUT BECAUSE IT TAKES A WHILE TO RUN
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


trips_per_day.plot.bar()
# plt.show()
"""

# Problem 9: Create Heatmap of trips by hour and day of week, where the x axis is days of the week and the y axis is hour of the day, and there are cells with the cumulative total of trips taken that weekday and within that hour. Then color the cells based on value, where the lowest are red, average are white, and darkest are green.

# find the name of a chart or display that could do this

# add column for weekday

# trips['Weekday'] = trips['Date'].apply(lambda n: pd.to_datetime(n).day_name())
# ^ LEFT OFF at this point the code is taking a while to run and the thing below is not printing. So my goal is to complete the operation of adding a column for the Weekday. I should try it on just a few rows to make sure it works befroe doiring on the whole table

"""Code I used to figure out how to get a column of weekdays. Using .apply() on every row was so slow it wasn't working. So instead I ran the .dt.day_name() on just the trips['Date/Time'] column. That was way faster.

# trips['Weekday'] = trips['Date'].apply(lambda n: pd.to_datetime(n).day_name())
# ^  at this point the code is taking a while to run and the thing below is not printing. So my goal is to complete the operation of adding a column for the Weekday. I should try it on just a few rows to make sure it works befroe doiring on the whole table

print((trips.iloc[0]['Date']))

print(pd.to_datetime(trips.iloc[0]['Date']))


print(pd.to_datetime(trips.iloc[0]['Date']).day_name())

print(pd.to_datetime(trips.iloc[0]['Date']).day_name())

# this line takes way too long to run
# trips['Weekday'] = trips['Date'].apply(lambda n: pd.to_datetime(trips.iloc[n]['Date']).day_name())
# """

trips['Date/Time'] = pd.to_datetime(trips['Date/Time'])
trips['Weekday'] = trips['Date/Time'].dt.day_name()






# LEFT OFF. Now that I have a column of weekdays, somehow I have to organize the aggreated total number of trips based on their value in the 'Hour' column and 'Weekday' column. Start by finding the number of trips for that have 'Hour' == 12 and 'Weekday' == 'Monday'. This will help me understand how to fetch that data. From there, I can store the data in a certain way that will allow me to create the heatmap.

# Wait after making trips_pivot, the rows of Hours weren't sorted properly, so their current order is 0,1,10,11,23,3,4,5... So for single digit hours, I'll have to add a zero before them.

def hour_format(hour: int) -> str:
    '''Takes a hour in the format of int , and if it's a single digit, it adds a zero before it and makes it a string'''
    
    hour_string = str(hour)
    
    if len(hour_string) == 1:
        formatted_hour = f"0{hour_string}"
    else:
        formatted_hour = hour_string
    
    return formatted_hour

# transform 'Hour' column using hour_format()
trips['Hour'] = trips['Hour'].apply(hour_format)

trips_pivot = trips.pivot_table(
    index='Hour',       # What becomes the rows
    columns='Weekday',         # What becomes the columns
    aggfunc='size'         # How to combine multiple values
).reindex(labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], axis = 1)
# the .reidex() reorders the x axis of weekdays so they appear chronologically, not alphabetically.


pd.set_option("display.max_rows", 59) #Make it so all rows are displayed in the terminal
print("Pivot table:")
print(trips_pivot)


# Now that I have this pivot table data displaying in my termianl correctly, ordered, I want to produce a heatmap where each cell value is colored based on the value. For values near the bottom of the range, I want them colored red. For values near the middle of the range, I want white. For values near the top of the range, I want green. I want the values color to be on a gradient according to what it's value is compared to the range of all cell values. For example, the minimum cell value should be the most red. The maximum cell value should be the most green. And the value closest to the mean of all the cell values should be closest to white

color_map = sns.diverging_palette(0, 120, s=80, l=55, center='light', as_cmap=True)

max_value_of_trips_pivot = trips_pivot.max().max() #expect 12369
min_value_of_trips_pivot = trips_pivot.min().min() #expect 597

print("Max: ")
print(max_value_of_trips_pivot)
print("Min: ")
print(min_value_of_trips_pivot)

trips_heatmap = sns.heatmap(data = trips_pivot, cmap = color_map, annot = True, linewidths = 10, linecolor = "black", center = 0)

# for the center, I need to create a variable that is defined as the average of the max and min values in trips_pivot

plt.show()
import pandas as pd

trips = pd.read_csv(r"C:\Repositories for Git\uber-trips-analysis-folder\uber-raw-data-sep14.csv")



#Problem 1: find busiest date

trips_by_day = trips.groupby('Date/Time')


trips['Date'] = trips['Date/Time'].apply(lambda n: n.split(' ')[0])
    # Adds a column to the trips table

busiest_date = trips['Date'].value_counts().idxmax()
most_trips_in_one_day = trips['Date'].value_counts().iloc[0]

busiest_day_message = f"The busiest date was {busiest_date}. It had {most_trips_in_one_day} trips."

print(busiest_day_message)



# Problem 2: Find time with lowest number of rides
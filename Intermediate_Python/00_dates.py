### Date ###

from datetime import timedelta, timedelta, timedelta, datetime as dt

now = dt.now()                          # new instance
print(f"date: {now}")                   # = date: 2022-11-22 11:21:10.324072
print(f"Year: {now.year}")              # = Year: 2022 
print(f"Month: {now.month}")            # = Month: 11  
print(f"Week day: {now.weekday()}")     # = Week day: 1
print(f"Day: {now.day}")                # = Day: 22   
print(f"Hour: {now.hour}")              # = Hour: 11
print(f"Minute: {now.minute}")          # = Minute: 21 
print(f"Second: {now.second}")          # = Second: 10

time_stamp= now.timestamp()             # value in float
print(time_stamp)                       # = 1669112470.324072

def print_date(date):               
    print(f"date: {date}")                      # = date: 2023-01-01 00:00:00
    print(f"time stamp: {date.timestamp()}")    # = time stamp: 1672527600.0
    
year_2023 = dt(2023, 1, 1)
print_date(year_2023)

# time
from datetime import time as time

current_time = time()
print(current_time.hour)                # = 0

current_time = time(23, 35, 21, 0)
print(current_time.hour)                # = 23


# date
from datetime import date as date

current_date = date.today()
print(current_date.year)                # = 2022

current_date = date(2023, 1, 1)
print(current_date.year)                # = 2023

current_date = date(current_date.year + 1, current_date.month, current_date.day)
print(current_date.year)                # = 2024

# working with datetime
diff = year_2023 - now
print(f"year_2023 - now result {diff}") # = year_2023 - now result 39 days, 12:04:58.318108

# working with date
diff = year_2023.date() - current_date
print(f"year_2023 - now result {diff}") # = year_2023 - now result -365 days, 0:00:00


# time delta
from datetime import timedelta as td

start_time_delta = td(200, 100, 100, weeks = 10)
end_time_delta = td(300, 100, 100, weeks = 13)
print(end_time_delta - start_time_delta) # = 121 days, 0:00:00
print(end_time_delta + start_time_delta) # = 661 days, 0:03:20.000200


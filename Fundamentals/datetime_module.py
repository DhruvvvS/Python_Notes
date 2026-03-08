# datetime module 
# The datetime module provides classes for manipulating dates and times.
# It allows you to work with dates and times in both simple and complex ways.

# Importing the datetime module
import datetime

# Creating a datetime object and printing manual given time and date
date = datetime.date(2024, 6, 1)  # Creating a date object
print(date)  # Output: 2024-06-01
time = datetime.time(14, 30, 0)  # Creating a time object
print(time)  # Output: 14:30:00

dt = datetime.datetime(2024, 6, 1, 14, 30, 0)  # Creating a datetime object simultaneously
print(dt)  # Output: 2024-06-01 14:30:00

# Getting the current date and time
current_date = datetime.date.today()  # Getting the current date    
print(current_date)  # Output: Current date in YYYY-MM-DD format
current_time = datetime.datetime.now()  # Getting the current date and time
print(current_time)  # Output: Current date and time in YYYY-MM-DD HH:MM:SS format

# Formatting dates and times
formatted_date = current_date.strftime("%B/%d/%Y")  # Formatting date as 'Month/Day/Year'
print(formatted_date)  # Output: Current date in 'Month/Day/Year' format   
formatted_time = current_time.strftime("%I:%M:%S %p")  # Formatting time as 'Hour:Minute:Second AM/PM'
print(formatted_time)  # Output: Current time in 'Hour:Minute:Second AM/PM' format

# format specifiers:
# %Y - Year with century (e.g., 2024)  
# %m - Month as a zero-padded decimal number (e.g., 06)
# %d - Day of the month as a zero-padded decimal number (e.g., 01)
# %B - Full month name (e.g., June)
# %I - Hour (12-hour clock) as a zero-padded decimal number (e.g., 02)
# %M - Minute as a zero-padded decimal number (e.g., 30)
# %S - Second as a zero-padded decimal number (e.g., 00)
# %p - AM or PM

# timedelta objects represent a duration, the difference between two dates or times.
# You can perform arithmetic operations with timedelta objects to manipulate dates and times.
from datetime import timedelta

delta = timedelta(days=7, hours=3, minutes=30)

future = datetime.now() + timedelta(days=10)
past   = datetime.now() - timedelta(weeks=2)

# Difference between two datetimes
d1 = datetime(2025, 1, 1)
d2 = datetime(2025, 3, 8)
diff = d2 - d1

print(diff.days)          # 66
print(diff.total_seconds()) # 5702400.0

# The datetime module also provides classes for working with time zones, such as tzinfo and timezone.
# Built-in (Python 3.9+)
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime.now(timezone.utc)
ist_now = datetime.now(ZoneInfo("Asia/Kolkata"))
ny_now  = datetime.now(ZoneInfo("America/New_York"))

# Convert between timezones
utc_dt = datetime(2025, 6, 15, 12, 0, tzinfo=timezone.utc)
ist_dt = utc_dt.astimezone(ZoneInfo("Asia/Kolkata"))
print(ist_dt)   # 2025-06-15 17:30:00+05:30

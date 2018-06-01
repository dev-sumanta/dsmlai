# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:22:06 2017

@author: Samar
"""

import datetime

# Time values are represented with the time class
# Times have attributes for hour, minute, second, and microsecond
#  They can also include time zone information

t = datetime.time(12, 34, 45)
print('{:d}:{:d}:{:d}'.format(t.hour, t.minute, t.second))
print('{}:{}:{}'.format(t.hour, t.minute, t.second))

# A time instance only holds values of time,
# and not a date associated with the time

# The min and max class attributes reflect the
# valid range of times in a single day

print('Earliest: ', datetime.time.min)
print('Latest: ', datetime.time.max)
print('Resoultion: ', datetime.time.resolution)

# Calendar date values are represented with the date class
# Instances have attributes for year, month, and day
# It is easy to create a date representing
# today’s date using the today() class method


today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

# from ordinal will give us a date from integer
print(datetime.date.fromordinal(today.toordinal()))

# the range of dates supported can be found with the min and max attributes
print('Earliest: ', datetime.date.min)
print('Latest: ', datetime.date.max)
print('Resoultion: ', datetime.date.resolution)

# replace is another method to create new date instances
print(today.replace(year=2020))

# date arithmetic can be carried out using timedeltas
# timedeltas can be specified as microseconds,
# milliseconds, seconds, minutes, hours, days, weeks
_1_hour_delta = datetime.timedelta(hours=1)
_1_day_delta = datetime.timedelta(days=1)
tomorrow = today + _1_day_delta
print(tomorrow)

# comparing dates
print('equal ', today == tomorrow)
print('< ', today < tomorrow)
print('> ', today > tomorrow)

# combining date times - datetime.datetime
dt_now = datetime.datetime.now()
print(dt_now)
_1_hour_delta = datetime.timedelta(hours=1)
_1_hour_hence = dt_now + _1_hour_delta
print(_1_hour_hence)
_1_day_hence_1_hour_before = dt_now + _1_day_delta - _1_hour_delta
print(_1_day_hence_1_hour_before)

# The default string representation of a datetime object
# uses the ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
# Alternate formats can be generated using strftime()

format = "%a %b %d %H:%M:%S %Y"
today_with_time = datetime.datetime.today()
print('ISO: ', today_with_time)
print(today_with_time.strftime(format))

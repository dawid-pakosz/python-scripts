import time
import datetime

from PIL.ImageChops import difference

#-----Get current time in seconds since the epoch as a floating-point number ---------------------------------------------
get_current_time = time.time()
print(f'Current Time: {get_current_time}')
#Current Time: 1764424663.3188384


#-----Get the current local time ---------------------------------------------
get_local_time = time.localtime(time.time())
print(f'Local time: {get_local_time}')
#Local time: time.struct_time(tm_year=2025, tm_mon=11, tm_mday=29, tm_hour=14, tm_min=57, tm_sec=43, tm_wday=5, tm_yday=333, tm_isdst=0)


#-----Convert times to readable formats ---------------------------------------------
get_readable_time_format = time.asctime()
print(get_readable_time_format)
#Sat Nov 29 15:22:42 2025


#----- High precision timing ---------------------------------------------
get_high_precision_timing = time.perf_counter()
print(get_high_precision_timing)
#289287.9094734


#----- Sum of the system and user CPU time of the current process ---------------------------------------------
get_sum_time = time.process_time()
print(get_sum_time)
#0.078125


#----- Calculate the difference between two dates or times ---------------------------------------------
today = datetime.date.today()
print(f'today is: {today}')
#today is: 2025-11-29

get_time_difference = today - datetime.timedelta(days=3)
print(f'Three days ago: {get_time_difference}')
# Three days ago: 2025-11-26



#----- Get current date and time ---------------------------------------------
get_current_date_and_time = datetime.datetime.now(tz=None)
print(get_current_date_and_time)                                                            # 2025-11-29 16:05:15.331358
print(f'datetime.datetime.today: {datetime.datetime.today()}')                              # 2025-11-29 16:05:15.331359
print(f'datetime.datetime.now: {datetime.datetime.now()}')                                  # 2025-11-29 16:05:15.331358
print(f'datetime.datetime.date: ({datetime.datetime.date(get_current_date_and_time)})')     # 2025-11-29
print(f'datetime.datetime.time: ({datetime.datetime.time(get_current_date_and_time)})')     # 16:07:48.453896



#----- Get a datetime object representing the specified ISO calendar date ---------------------------------------------
# iso_year

iso_weekday = datetime.datetime.weekday(get_current_date_and_time)
iso_day = datetime.datetime.isoweekday(get_current_date_and_time)
print(iso_day)


# get_specific_iso_calendar_date = datetime.datetime.isocalendar(2025,11,3)
# print(get_specific_iso_calendar_date)


#----- XXXXXXXX ---------------------------------------------

print()


#----- XXXXXXXX ---------------------------------------------

print()


#----- XXXXXXXX ---------------------------------------------

print()


#----- XXXXXXXX ---------------------------------------------

print()










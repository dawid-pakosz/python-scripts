import time

#Get current time in seconds since the epoch as a floating-point number
get_current_time = time.time()
print(f'Current Time: {get_current_time}')
#Current Time: 1764424663.3188384


#Get the current local time
get_local_time = time.localtime(get_current_time)
print(f'Local time: {get_local_time}')
#Local time: time.struct_time(tm_year=2025, tm_mon=11, tm_mday=29, tm_hour=14, tm_min=57, tm_sec=43, tm_wday=5, tm_yday=333, tm_isdst=0)


#Convert times to readable formats
from utils.required_apis import *

# Seven days are taken from each season and then averaged
SPRING = ['2021-03-20', '2021-03-27', '2021-04-03', '2021-04-24', '2021-05-01',
'2021-05-29', '2021-06-08']

SUMMER = ['2021-06-21', '2021-06-26', '2021-07-10', '2021-07-24', '2021-08-01',
'2021-08-29', '2021-09-05']

FALL = ['2021-09-22', '2021-10-10', '2021-10-30', '2021-11-07', '2021-11-25',
'2021-12-05', '2021-12-19']

WINTER = ['2021-12-22', '2022-01-10', '2022-01-30', '2022-02-07', '2022-02-25',
'2022-03-05', '2022-03-17']

# Convert time to mins
def convert_time_to_mins(date):
    time = daylight_api.retrieve_day_light(date)
    total_mins = 0
    list_time = time.split(':')

    hours = int(list_time[0])
    mins = int(list_time[1])
    seconds = int(list_time[2])

    hours *= 60
    seconds = seconds / 100
    total_mins = hours + mins + seconds

    return total_mins

# Find average
def find_avg(list):
    return sum(list) / len(list)

# Convert mins back to hours & mins
def convert_mins_to_hours(mins):
    hours = mins / 60
    
    return round(hours, 2)

# Gets the average daylight time in hours for each season
avg_spring = convert_mins_to_hours(find_avg([convert_time_to_mins(i) for i in SPRING]))
avg_summer = convert_mins_to_hours(find_avg([convert_time_to_mins(i) for i in SUMMER]))
avg_fall = convert_mins_to_hours(find_avg([convert_time_to_mins(i) for i in FALL]))
avg_winter = convert_mins_to_hours(find_avg([convert_time_to_mins(i) for i in WINTER]))



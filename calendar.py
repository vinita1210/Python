import calendar

date_main = raw_input()
mnth,date,year = date_main.split()
mnth = int(mnth)
date = int(date)
year = int(year)
#print calendar.TextCalendar(firstweekday=6).formatyear(year)
day_num = calendar.weekday(year,mnth,date)

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", 
                         "FRIDAY", "SATURDAY", "SUNDAY"] 
print(days[day_num])                         

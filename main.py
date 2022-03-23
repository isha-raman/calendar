import calendar
print(calendar.weekheader(3))
print()
print(calendar.firstweekday()) #python starts week by monday
print()
print(calendar.month(2000,9,w=3,l=1))
print()
print(calendar.monthcalendar(2022,3)) #in aray form
print()
print(calendar.calendar(1974))
print()
day_of_the_week = calendar.weekday(3000,12,4)
print(day_of_the_week)
print()
print(calendar.isleap(2000))
print()
how_many_leap_days = calendar.leapdays(2000,3000) #it ignores 3000:y2 so if you need to include 3000 type 3001
print(how_many_leap_days)
print()
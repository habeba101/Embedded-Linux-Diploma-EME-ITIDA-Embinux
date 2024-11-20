# Print the calendar of a given month and year?

# (you give it the year and the month and it should print the calendar of that month)
from calendar import TextCalendar

tc=TextCalendar(firstweekday=0)

year=int(input("Enter the year"))
month=int(input("Enter the month"))

tc.prmonth(year,month)

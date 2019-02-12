"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

# - Dependencies --------------------------------
import sys
import calendar
from datetime import datetime

# - Project Constants ---------------------------
ERROR_PARAMETERS_INCORRECT = "Please provide only Month (int) and Year (int)"

# - Determine Month and Year to Display ---------
# Set defaults
default_date = datetime.now()
user_month = default_date.month
user_year = default_date.year
# Exit program if user mangled arguments
user_arguments_length = len(sys.argv)
if(user_arguments_length > 3):
    print(ERROR_PARAMETERS_INCORRECT)
    exit(1)
# Set month and year to user input, if provided
if(user_arguments_length >= 3):
    user_year = int(sys.argv[2])
if(user_arguments_length >= 2):
    user_month = int(sys.argv[1])

# - Display Calendar to user --------------------
calendar_string = calendar.month(user_year, user_month)
print(calendar_string)

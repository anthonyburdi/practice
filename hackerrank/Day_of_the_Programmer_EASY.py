# Day_of_the_Programmer_EASY.py

# hackerrank.com/challenges/day-of-the-programmer/problem

# Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the  day of the year) during a year in the inclusive range from  to .

# From  to , Russia's official calendar was the Julian calendar; since  they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in , when the next day after January  was February . This means that in , February  was the  day of the year in Russia.

# In both calendar systems, February is the only month with a variable amount of days; it has  days during a leap year, and  days during all other years. In the Julian calendar, leap years are divisible by ; in the Gregorian calendar, leap years are either of the following:

# Divisible by .
# Divisible by  and not divisible by .
# Given a year, , find the date of the  day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .

# For example, the given .  is divisible by , so it is a leap year. The  day of a leap year after  is September 12, so the answer is .

# Function Description

# Complete the dayOfProgrammer function in the editor below. It should return a string representing the date of the  day of the year given.

# dayOfProgrammer has the following parameter(s):

# year: an integer
# Input Format

# A single integer denoting year .

# Constraints

# Output Format

# Print the full date of Day of the Programmer during year  in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .

# Sample Input 0

# 2017
# Sample Output 0

# 13.09.2017
# Explanation 0

# In the year , January has  days, February has  days, March has  days, April has  days, May has  days, June has  days, July has  days, and August has  days. When we sum the total number of days in the first eight months, we get . Day of the Programmer is the  day, so then calculate  to determine that it falls on day  of the  month (September). We then print the full date in the specified format, which is 13.09.2017.

# Sample Input 1

# 2016
# Sample Output 1

# 12.09.2016
# Explanation 1

# Year  is a leap year, so February has  days but all the other months have the same number of days as in . When we sum the total number of days in the first eight months, we get . Day of the Programmer is the  day, so then calculate  to determine that it falls on day  of the  month (September). We then print the full date in the specified format, which is 12.09.2016.

# Sample Input 2

# 1800
# Sample Output 2

# 12.09.1800
# Explanation 2

# Since 1800 is leap year. Day lies on 12 September.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    # Assumptions
    # all data fits on a single machine
    # 1700 <= y <= 2700

    # Approach, Complexity, Tradeoffs, Potential Improvements
    # Create a function for num_days_in_feb
    # Create a function for month
    # Create a function for leftover days
    # return month, leftover days and year
    # Num days in feb just checks a few criteria
    # month function adds up days of the months in that year and returns
    # the month before going over 256
    # Leftover days returns the days in the months added up in the month
    # function subtracted from 256
    # All of these operations are constant time and space so O(1) in both
    # time and space for complexity
    # I can't think of any way to improve this other than to extend it
    # so other calendars could be used but that seems unnecessary - we can
    # also easily just modify the function

    # Edge Cases
    # 1919, 1918, 1917, 1700, 2700

    DAY_OF_YR = 256

    def num_days_in_feb(year: int) -> int:
        """Num days in feb based on the calendar in force that year."""

        if year <= 1917:
            # Julian
            if year % 4 == 0:
                return 29
            else:
                return 28

        elif year == 1918:
            # Transitional
            return 15

        elif year >= 1919:
            # Gregorian
            if (year % 400 == 0) or ((year % 4 == 0) and (not year % 100 == 0)):
                return 29
            else:
                return 28


    def month_of_day_of_programmer(year: int) -> int:
        """Return the month, day of the day of the programmer."""

        feb = num_days_in_feb(year)
        days_in_months = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        tot_days = 0

        for i, days in enumerate(days_in_months):
            tot_days += days
            if tot_days > DAY_OF_YR:
                return i + 1, DAY_OF_YR - (tot_days - days)
            if tot_days == DAY_OF_YR:
                return i, days

    month, day = month_of_day_of_programmer(year)

    return "{:02d}.{:02d}.{}".format(day, month, year)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

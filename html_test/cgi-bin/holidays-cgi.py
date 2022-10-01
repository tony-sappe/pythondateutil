#!/usr/bin/env python
#  holidays-cgi.py: -*- Python -*-  DESCRIPTIVE TEXT.
#
#  Author: Phil Schwartz (phil.schwartz@users.sourceforge.net)
#  Date: Tue Jan 21 10:11:35 2003.

import cgi
import holidays
import time

from calendar import SUNDAY
from calendar import *

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def print_calendar(year, month, day):
    # print a calendar for M/D/Y where D is highlighted in blue.

    setfirstweekday(SUNDAY)
    month_cal = monthcalendar(year, month)

    print("<table border=1>\n")
    print(
        f"<tr><td colspan=7><font color=blue><center>{MONTHS[month - 1]} {year}</font></center></td></tr>"
    )
    print("<tr><td>S</td><td>M</td><td>T</td><td>W</td><td>T</td><td>F</td><td>S</td></tr>")
    for week in month_cal:
        print("<tr>")
        for monthday in week:
            if monthday == 0:
                print("<td>&nbsp;</td>")
                continue
            if monthday == day:
                color = "blue"
            else:
                color = "black"

            print(f"<td><font color={color}>{monthday}</td>")
        print("</tr>")
    print("</table>\n")


##########################################################################################

form = cgi.FieldStorage()
print("Content-Type: text/html\n\n")
print("<html><head></head>\n")
print("<body bgcolor=white>\n")

failed = 0

try:
    year = int(form["year"].value)
except Exception:
    failed = 1
    print("Year must be an integer<p>\n")

try:
    holiday_func = form["holiday"].value
    if not holiday_func:
        raise Exception
except Exception:
    failed = 1
    print("You must select a holiday from the list<P>\n")

if not failed:
    print("<center>\n")
    holiday_obj = holidays.Holidays(year)
    func = eval(f"holiday_obj.{holiday_func}")
    apply(func, ())
    tm = holiday_obj.get_tuple()

    format_str = "%A, %B %d, %Y"
    print(f"The holiday falls on: <font color=blue>{time.strftime(format_str, tm)}</font>")
    print("<p>\n")
    print_calendar(tm[0], tm[1], tm[2])
    print("</center>\n")


print("</body></html>")

from ctypes import cdll
import datetime

color_lib = cdll.LoadLibrary("./libcolors.so")

# Get a datetime object which represents Christmas day
christmas = datetime.date(2023, 12, 25)

# Subtract the current datetime from Christmas
christmas_delta = christmas - datetime.datetime.now().date()

# You can find the definition for the functions in this library in colors.c

# cprintf(const char *format, ...)
color_lib.cprintf("&(red)&&(_green)&Happy Holidays!\n".encode())

# Note that after Christmas has passed, this will print a negative number
color_lib.cprintf("&(blue)&&(_green)&Only %d days until Christmas\n".encode(), christmas_delta.days)

# Note the `.encode()` at the end of the above string arguments ^
# This is because Python uses "wide" characters, whereas printf expects utf-8 encoded bytes
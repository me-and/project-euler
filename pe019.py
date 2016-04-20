#!/usr/bin/env python3
'''
Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
'''

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')


class Month(object):
    def __init__(self, name, year, start_day):
        self.name = name
        self.year = year
        self.length = self.get_length()
        self.start_day = start_day

    def get_length(self):
        if self.name in ('January', 'March', 'May', 'July', 'August',
                         'October', 'December'):
            return 31
        elif self.name in ('April', 'June', 'September', 'November'):
            return 30
        elif (self.name == 'February' and
              self.year % 4 == 0 and (self.year % 100 != 0 or
                                      self.year % 400 == 0)):
            return 29
        elif self.name == 'February':
            return 28
        else:
            raise RuntimeError('Unexpected month: {!r}'.format(name))

    def get_start_day_of_next_month(self):
        return DAYS[(DAYS.index(self.start_day) + self.length) % 7]

if __name__ == '__main__':
    # We're given starting information for 1 January 1900, but we need to get
    # through 1900 to 1901 before we start counting.
    this_month = Month('January', 1900, 'Monday')
    for month_name in MONTHS[1:]:
        this_month = Month(month_name, 1900,
                           this_month.get_start_day_of_next_month())

    sundays = 0
    for year in range(1901, 2001):
        for month_name in MONTHS:
            this_month = Month(month_name, year,
                               this_month.get_start_day_of_next_month())
            if this_month.start_day == 'Sunday':
                sundays += 1
    print(sundays)

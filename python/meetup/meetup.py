from datetime import *

def meetup_day(year, month, day_of_the_week, which):

    week_dict = {"1st":0,"2nd":1,"3rd":2,"4th":3,"5th":4,"last":-1}

    days_dict = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[], "Sunday":[]}

    dt = date(year, month, 1)

    while dt.month == month:
        day = dt.strftime('%A')
        days_dict[day].append(dt.day)
        dt = dt + timedelta(days=1)

    try:
        if which != "teenth":
            date_index = week_dict.get(which)
            day_num = days_dict.get(day_of_the_week)[date_index]
            return date(year, month, day_num)
        else:
            dates_list = days_dict.get(day_of_the_week)
            for day_num in dates_list:
                if day_num > 12 and day_num < 20:
                    return date(year, month, day_num)
    except:
        raise MeetupDayException("Are you sure thats a valid date?")


class MeetupDayException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


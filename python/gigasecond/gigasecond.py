import datetime


def add_gigasecond(birth_date):

    giga_date = birth_date + datetime.timedelta(seconds=1000000000)

    return giga_date




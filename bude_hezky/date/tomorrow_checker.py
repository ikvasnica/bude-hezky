import datetime

def is_tomorrow(datetime, tomorrow_date=None):
    tomorrow_date = tomorrow_date or (datetime.date.today() + datetime.timedelta(days=1))

    return tomorrow_date == datetime.date()
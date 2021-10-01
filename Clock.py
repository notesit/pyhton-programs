# Clock
import time


def current_time():
    # Get the Current Time with pm or am, Day and Date
    hr = str(time.strftime('%I'))
    min = str(time.strftime('%M'))
    sec = str(time.strftime('%S'))
    noon = str(time.strftime('%p'))
    month = str(time.strftime('%b'))
    date = str(time.strftime('%d'))
    year = str(time.strftime('%y'))
    day = str(time.strftime('%A'))

    return hr, min, sec, noon, date, month, year, day

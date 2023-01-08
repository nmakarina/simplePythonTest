from datetime import datetime
from datetime import timedelta


def getCurrentDateStr():
    now = datetime.now()
    return now.strftime("%d.%m.%Y")


def getNextDateStr():
    now = datetime.now()
    delta = timedelta(days=1)
    date = now + delta
    return date.strftime("%d.%m.%Y")
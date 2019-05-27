import datetime
import math


def cost_raw(rates: dict,
             start: datetime.datetime,
             end: datetime.datetime):
    duration = end - start

    if duration.total_seconds() < 2160:  # 36 min
        cost = math.ceil(duration.total_seconds() / 60) * rates['minute']

    elif duration.total_seconds() <= 21600: # 6 hours
        cost = math.ceil(duration.total_seconds() / 3600) * rates['hour']

    else:
        cost = math.ceil(duration.total_seconds() / 86400) * rates['day']

    return cost + rates['access_fee']


def calculate_taxes():
    pass


def best_rate():
    pass

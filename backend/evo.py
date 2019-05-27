import math
import datetime
import os

dirname = os.path.dirname(__file__)
DATA_INPUT = os.path.join(dirname, 'data', 'evo.json')


def get_inputs(input):
    import json
    with open(input) as file:
        return json.load(file)


inputs = get_inputs(DATA_INPUT)


def cost_raw(rates: dict,
             start: datetime.datetime,
             end: datetime.datetime):
    duration = end - start

    if duration.total_seconds() < 2160:  # 36 min
        cost = math.ceil(duration.total_seconds() / 60) * rates['minute']

    elif duration.total_seconds() <= 21600:  # 6 hours
        cost = math.ceil(duration.total_seconds() / 3600) * rates['hour']

    else:
        cost = math.ceil(duration.total_seconds() / 86400) * rates['day']

    return cost + rates['access_fee']


def calculate_taxes(taxes: dict,
                    hours: int,
                    raw_cost: float) -> dict:
    if hours < 8:
        pvrt = 0
    else:
        pvrt = int(max(1, hours / 24)) * taxes['pvrt']

    gst = (raw_cost + pvrt) * taxes['gst'] / 100
    pst = (raw_cost + pvrt) * taxes['pst'] / 100

    total = gst + pst + pvrt + raw_cost

    return ({
        "raw": round(raw_cost, 2),
        "pvrt": round(pvrt, 2),
        "gst": round(gst, 2),
        "pst": round(pst, 2),
        "total": round(total, 2)
    })


def cost_taxes_included(
        rates: dict,
        taxes: dict,
        start: datetime.datetime,
        end: datetime.datetime):

    duration = end - start
    hours = int((duration.days * 24) + (duration.seconds / 3600))

    raw_cost = cost_raw(rates,start,end)
    return calculate_taxes(taxes,hours,raw_cost)
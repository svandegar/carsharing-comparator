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
        best_rate = 'Minute'

    elif duration.total_seconds() <= 21600:  # 6 hours
        cost = math.ceil(duration.total_seconds() / 3600) * rates['hour']
        best_rate = 'Hour'

    else:
        cost = math.ceil(duration.total_seconds() / 86400) * rates['day']
        best_rate = 'Day'

    return {'rate': best_rate,
            'cost': cost + rates['access_fee']}


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
        inputs: dict,
        start: datetime.datetime,
        end: datetime.datetime):
    duration = end - start
    hours = int((duration.days * 24) + (duration.seconds / 3600))

    raw_cost = cost_raw(inputs['rates'], start, end)
    return {
        'rate':raw_cost['rate'] ,
        'cost' :calculate_taxes(inputs['taxes'], hours, raw_cost['cost'])}

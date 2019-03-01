import datetime
import os
import json
from backend import modo

# get inputs
dirname = os.path.dirname(__file__)
DATA_INPUT = os.path.join(dirname, 'test_data', 'test_modo.json')

with open(DATA_INPUT) as file:
    inputs = json.load(file)

    rates = inputs['rates']
    night = inputs['night']
    taxes = inputs['taxes']

inputs = dict(night=night, rates=rates, taxes=taxes)

# normal rate
start1 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end1 = datetime.datetime(year=2018, month=12, day=24, hour=10, minute=0)

# multiple days rate
start2 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end2 = datetime.datetime(year=2018, month=12, day=29, hour=10, minute=0)

# night rate
start3 = datetime.datetime(year=2018, month=12, day=24, hour=19, minute=0)
end3 = datetime.datetime(year=2018, month=12, day=25, hour=7, minute=0)


# test

def test_cost_raw_monthly():
    assert (modo.cost_raw('monthly',
                          rates,
                          night,
                          distance=79,
                          start=start1,
                          end=end1,
                          passengers=2) == 54)

    assert (modo.cost_raw('monthly',
                          rates,
                          night,
                          distance=79,
                          start=start2,
                          end=end2,
                          passengers=2) == 414)

    assert (modo.cost_raw('monthly',
                          rates,
                          night,
                          distance=20,
                          start=start3,
                          end=end3,
                          passengers=2) == 27)


def test_cost_raw_plus():
    assert (modo.cost_raw('plus',
                          rates,
                          night,
                          distance=79,
                          start=start1,
                          end=end1,
                          passengers=2) == 53.7)

    assert (modo.cost_raw('plus',
                          rates,
                          night,
                          distance=79,
                          start=start2,
                          end=end2,
                          passengers=2) == 303.7)

    assert (modo.cost_raw('plus',
                          rates,
                          night,
                          distance=20,
                          start=start3,
                          end=end3,
                          passengers=2) == 21)


def test_calculate_taxes():
    assert (modo.calculate_taxes(
        taxes=taxes,
        hours=6,
        raw_cost=53.7) == {
                "raw": 53.7,
                "gst": 2.69,
                "pst": 3.76,
                "pvrt": 0,
                "total": 60.14
            })

    assert (modo.calculate_taxes(
        taxes=taxes,
        hours=126,
        raw_cost=303.7) == {
                "raw": 303.7,
                "gst": 15.56,
                "pst": 21.78,
                "pvrt": 7.5,
                "total": 348.54
            })


def test_best_rate():
    assert (modo.best_rate(inputs,
                           distance=79,
                           start=start1,
                           end=end1,
                           passengers=2) == {
                "rate": "plus",
                "cost": {
                    "raw": 53.7,
                    "gst": 2.69,
                    "pst": 3.76,
                    "pvrt": 0,
                    "total": 60.14
                }
            })

    assert (modo.best_rate(inputs,
                           distance=100,
                           start=start1,
                           end=end1,
                           passengers=2) == {
                "rate": "monthly",
                "cost": {
                    "raw": 54,
                    "gst": 2.7,
                    "pst": 3.78,
                    "pvrt": 0,
                    "total": 60.48
                }
            })

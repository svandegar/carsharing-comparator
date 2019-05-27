from backend import evo
import datetime
import os
import json

# get inputs
dirname = os.path.dirname(__file__)
DATA_INPUT = os.path.join(dirname, 'test_data', 'test_evo.json')

with open(DATA_INPUT) as file:
    inputs = json.load(file)
    rates = inputs['rates']
    taxes = inputs['taxes']

# minute rate
start1 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end1 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=25)

# hour rate
start2 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end2 = datetime.datetime(year=2018, month=12, day=24, hour=9, minute=5)

# day rate
start3 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end3 = datetime.datetime(year=2018, month=12, day=25, hour=4, minute=0)


# test
def test_cost_raw():
    assert evo.cost_raw(rates=rates,
                        start=start1,
                        end=end1
                        ) == 10.25 + 1

    assert evo.cost_raw(rates=rates,
                        start=start2,
                        end=end2
                        ) == 89.94 + 1

    assert evo.cost_raw(rates=rates,
                        start=start3,
                        end=end3
                        ) == 89.99 + 1


def test_calculate_taxes():
    assert evo.calculate_taxes(
        taxes=taxes,
        hours=2,
        raw_cost=10) == {
               "raw": 10,
               "gst": 0.5,
               "pst": 0.7,
               "pvrt": 0,
               "total": 11.2
           }

    assert evo.calculate_taxes(
        taxes=taxes,
        hours=32,
        raw_cost=97) == {
               "raw": 97,
               "gst": 4.92,
               "pst": 6.89,
               "pvrt": 1.5,
               "total": 110.32
           }

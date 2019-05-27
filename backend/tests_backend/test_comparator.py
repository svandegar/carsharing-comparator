from backend import comparator
import os
import datetime

dirname = os.path.dirname(__file__)
MODO_INPUT = os.path.join(dirname, 'test_data', 'test_modo.json')
EVO_INPUT = os.path.join(dirname, 'test_data', 'test_evo.json')

inputs = {}


def get_inputs(input):
    import json
    with open(input) as file:
        return json.load(file)


inputs['Modo'] = get_inputs(MODO_INPUT)


def get_inputs(input):
    import json
    with open(input) as file:
        return json.load(file)


inputs['Evo'] = get_inputs(EVO_INPUT)

# minute rate
start1 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end1 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=25)

# hour rate
start2 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end2 = datetime.datetime(year=2018, month=12, day=24, hour=9, minute=5)

# day rate
start3 = datetime.datetime(year=2018, month=12, day=24, hour=4, minute=0)
end3 = datetime.datetime(year=2018, month=12, day=25, hour=4, minute=0)


def test_compare():
    assert comparator.compare(
        inputs,
        135,
        start1,
        end1,
        passengers=4,
        car_type='normal',
        one_way=False
    ) == {'company': 'Modo',
          'result': {'cost':
                         {'gst': 0.19,
                          'pst': 0.26,
                          'pvrt': 0,
                          'raw': 3.75,
                          'total': 4.2
                          },
                     'rate': 'monthly'}}


test_compare()

import datetime
import os
dirname = os.path.dirname(__file__)
DATA_INPUT = os.path.join(dirname, 'data','taxes.json')


def get_inputs(input):
        import json
        with open(input) as file:
            return json.load(file)

taxes = get_inputs(DATA_INPUT)



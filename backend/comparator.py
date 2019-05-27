from backend import modo, evo


def compare(inputs, distance, start, end, passengers: int, car_type: str = None, one_way=False):
    results = {}
    results['Modo'] = modo.best_rate(inputs['Modo'], distance, start, end, passengers, car_type)
    results['Evo'] = evo.cost_taxes_included(inputs['Evo'], start, end)

    if passengers > 4:
        results.pop('Evo')

    if one_way:
        results.pop('Modo')

    minimum_result = {'cost':{'total': float('inf')}}
    minimum_company = ''

    for key, value in results.items():
        if value['cost']['total'] < minimum_result['cost']['total']:
            minimum_result = value
            minimum_company = key

    return {
        'company': minimum_company,
        'result': minimum_result
    }

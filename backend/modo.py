import datetime


def cost_raw(subscription: str,
             rates: dict,
             night: dict,
             distance: int,
             start: datetime.datetime,
             end: datetime.datetime,
             passengers: int,
             type='normal') -> int:
    """
    Return the rate for Modo Monthly members, given the passed arguments
    :param rates: dict: rates
    :param night: dict: night hours
    :param distance: int: kilometers
    :param start: datetime: start of the renting
    :param end: datetime: end of the renting
    :param passengers: int: number of passengers, driver not included
    :param type: str: type of car : normal, large&loadable or oversize&premium. Default = normal.
    If passengers > 4, type if always large&loadable
    :return: int: raw price
    """
    duration = end - start
    duration_hours = (duration.days * 24) + (duration.seconds / 3600)
    applicable_rates = rates[subscription]

    # select car type
    if passengers > 4:
        type_rates = applicable_rates['large&loadable']
    else:
        type_rates = applicable_rates[type]

    # calculated the rate based on duration
    if duration_hours < 24:

        # night rate
        if start.time() >= datetime.time(night['from']) and end.time() <= datetime.time(night['to']):
            time_cost = type_rates['night']

        # normal rate
        else:
            time_cost = min(duration_hours * type_rates['hour'], type_rates['day'])

    else:
        days = int(duration_hours / 24)
        hours = duration_hours % 24
        time_cost = days * type_rates['day'] + min(hours * type_rates['hour'], type_rates['day'])

    # calculate the rate based on kilometers
    km = max(0, distance - rates[subscription]['free_km'])
    km_cost = km * rates[subscription]['km']

    return km_cost + time_cost


def calculate_taxes(taxes: dict, hours: int, raw_cost: float) -> dict:
    if hours < 8:
        pvrt = 0
    else:
        pvrt = int(max(1, hours / 24)) * taxes['pvrt']

    gst = (raw_cost + pvrt) * taxes['gst'] / 100
    pst = (raw_cost + pvrt) * taxes['pst'] / 100

    total = gst + pst + pvrt + raw_cost

    return ({
        "raw": round(raw_cost,2),
        "pvrt": round(pvrt, 2),
        "gst": round(gst, 2),
        "pst": round(pst, 2),
        "total": round(total, 2)
    })


def best_rate(
        rates: dict,
        night: dict,
        taxes: dict,
        distance: int,
        start: datetime.datetime,
        end: datetime.datetime,
        passengers: int,
        type='normal') -> dict:
    monthly = cost_raw('monthly',rates,night,distance,start,end,passengers,type)
    plus = cost_raw('plus',rates,night,distance,start,end,passengers,type)

    duration = end - start
    hours = int((duration.days * 24) + (duration.seconds / 3600))

    if monthly <= plus :
        return {
            "rate" : "monthly",
            "cost" : calculate_taxes(taxes,hours,monthly)
        }
    else:
        return {
            "rate": "plus",
            "cost": calculate_taxes(taxes, hours, plus)
        }
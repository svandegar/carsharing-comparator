import datetime
from backend import modo

# Set parameters

night = {
    "from": 19,
    "to": 9}

rates = {
    "monthly": {
        "km": 0.3,
        "free_km": 250,
        "normal": {
            "hour": 9,
            "day": 72,
            "night": 27
        },
        "large&loadable": {
            "hour": 10,
            "day": 80,
            "night": 30

        },
        "oversize&premium": {
            "hour": 14,
            "day": 112,
            "night": 42
        },

    },
    "plus": {
        "km": 0.3,
        "free_km": 0,
        "normal": {
            "hour": 5,
            "day": 50,
            "night": 15
        },
        "large&loadable": {
            "hour": 6,
            "day": 60,
            "night": 18

        },
        "oversize&premium": {
            "hour": 10,
            "dayh": 100,
            "night": 30
        },

    }
}
taxes = {
    "gst": 5,
    "pst": 7,
    "pvrt": 1.5
}

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
    assert (modo.best_rate(rates,
                           night,
                           taxes,
                           distance=79,
                           start=start1,
                           end=end1,
                           passengers=2) == {
                "rate": "plus",
                "cost": {
                    "raw":53.7,
                    "gst": 2.69,
                    "pst": 3.76,
                    "pvrt": 0,
                    "total": 60.14
                }
            })

    assert (modo.best_rate(rates,
                           night,
                           taxes,
                           distance=100,
                           start=start1,
                           end=end1,
                           passengers=2) == {
                "rate": "monthly",
                "cost": {
                    "raw":54,
                    "gst": 2.7,
                    "pst": 3.78,
                    "pvrt": 0,
                    "total": 60.48
                }
            })

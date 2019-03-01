from flask import render_template, request, flash
import backend
from website import app
from website.utils import forms


# get inputs :
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


@app.route('/', methods=['GET', 'POST'])
def home():
    form = forms.InputForm(request.form)
    print(type(form.end.data))
    if request.method == 'POST' and form.validate():
        rate = backend.modo.best_rate(
                    rates,
                    night,
                    taxes,
                    distance=form.distance.data,
                    start=form.start.data,
                    end=form.end.data,
                    passengers=form.passengers.data
                )

        return render_template('home.html',form=form, rate=rate)
    print(form.validate())
    return render_template('home.html', form=form)


@app.route('/test')
def test():
    return render_template('test.html')
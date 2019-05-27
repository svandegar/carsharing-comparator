from flask import render_template, request, flash
import backend
from website import app
from website.utils import forms


@app.route('/', methods=['GET', 'POST'])
def home():
    form = forms.InputForm(request.form)
    if request.method == 'POST' and form.validate():
        rate = backend.modo.best_rate(
                    backend.backend.modo.inputs,
                    distance=form.distance.data,
                    start=form.start.data,
                    end=form.end.data,
                    passengers=form.passengers.data
                )

        return render_template('home.html',form=form, rate=rate)

    return render_template('home.html', form=form)

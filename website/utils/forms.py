from wtforms import Form, validators, DateTimeField, IntegerField


class InputForm(Form):
    start = DateTimeField('Departure')
    end = DateTimeField('Return')
    distance = IntegerField('Distance [km]', [validators.DataRequired()])
    passengers = IntegerField('Number of passengers',
                              [validators.DataRequired(),
                               validators.number_range(0, 7, message="Must be between 0 and 7")])
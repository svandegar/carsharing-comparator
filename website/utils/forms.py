from wtforms import Form, validators, DateTimeField, IntegerField
import datetime

class InputForm(Form):
    start = DateTimeField( '',default=datetime.datetime.now(), format= '%Y-%m-%d %H:%M')
    end = DateTimeField('',default=datetime.datetime.now(), format = '%Y-%m-%d %H:%M')
    distance = IntegerField('Distance [km]', [validators.DataRequired()])
    passengers = IntegerField('Number of passengers',
                              [validators.DataRequired(),
                               validators.number_range(0, 7, message="Must be between 0 and 7")])
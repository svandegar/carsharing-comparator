from flask import Flask


app = Flask(__name__)

# TODO : remove this key from here
app.secret_key = 'foo'

from website import *
import backend
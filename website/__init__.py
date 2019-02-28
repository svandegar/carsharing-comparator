from flask import Flask

app = Flask(__name__)

app.secret_key = 'foo'

from website import *
import backend
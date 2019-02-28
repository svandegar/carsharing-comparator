from flask import Flask
import os

app = Flask(__name__)

# TODO : remove this key from here
app.secret_key = os.environ['SECRET_KEY']

from website import *
import backend
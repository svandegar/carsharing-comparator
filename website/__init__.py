from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']

from website import *
import backend
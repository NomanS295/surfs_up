import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

app = Flask(__name__)
# Define the welcome route

@app.route('/')
def hello_world():
    return 'Hello world'
    export FLASK_APP=app.py
# region
import numpy as np
import pandas as pd
import datetime as dt
from config import Config
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

# endregion

# initial setup of database and engine
engine = create_engine("sqlite:///data/fk8_data.sqlite", echo=False)
con = engine.connect()

Session = sqlalchemy.orm.sessionmaker(engine)
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
# gfb = Base.classes.gfb
# long_term = Base.classes.long_term




# Flask setup
app = Flask(__name__)
app.config.from_pyfile('config.py')

# routes
@app.route("/")
def index():
    """List all available apis"""

    return (
        f'Available Routes:<br/>'
        f'/function<br/>'
        f'/scatter<br/>'
        f'/tc<br/>'
        # f'/api/v1.0/<start><br/>'
        # f'/api/v1.0/<start>/<end><br/>'
        #  render_template('g_scatter.html')
    )


@app.route('/function')
def function():
    return render_template('multi_js1.html')



@app.route('/scatter')
def scatter():
    return render_template('scatter_js.html')


@app.route('/tc')
def tc():
    return render_template('tc_js.html')


if __name__ == '__main__':
    app.run(debug=True)

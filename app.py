
# from flask import Flask, render_template
# import pandas as pd
# import json
# import plotly
# import plotly.express as px
#
# app = Flask(__name__)
#
#
# # app.config.from_object('config.Config')
#
#
# @app.route('/')
# def g_scatter():
#     df = pd.read_csv('data/highest_gforce_boost_filtered.csv')
#     df = df[['frame', 'G.Lat', 'G.Long']]
#
#     fig = px.scatter(
#         df,
#         x='G.Lat',
#         y='G.Long',
#         animation_frame='frame'
#     )
#     print('hello')
#     graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return graph_json
#     # return render_template('index.html', graphJSON=graph_json)
#
#
# def hello():
#     """List all available apis"""
#
#     return (
#         f'Available Routes:<br/>'
#         f'/api/v1.0/precipitation<br/>'
#         f'/api/v1.0/stations<br/>'
#         f'/api/v1.0/tobs<br/>'
#         f'/api/v1.0/<start><br/>'
#         f'/api/v1.0/<start>/<end><br/>'
#     )
#
#
# if __name__ == '__main__':
#     app.run()

# imports
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

# Session = sqlalchemy.orm.sessionmaker(engine)
# reflect an existing database into a new model
# Base = automap_base()

# reflect the tables
# Base.prepare(engine, reflect=True)

# Save references to each table
# Fk8 = Base.classes.iats


# Create our session (link) from Python to the DB

# Flask setup
app = Flask(__name__)
app.config.from_pyfile('config.py')

# routes
@app.route("/")
def hello():
    """List all available apis"""

    return (
        f'Available Routes:<br/>'
        f'/api/function<br/>'
        f'/api/scatter<br/>'
        # f'/api/v1.0/tobs<br/>'
        # f'/api/v1.0/<start><br/>'
        # f'/api/v1.0/<start>/<end><br/>'
        #  render_template('g_scatter.html')
    )


@app.route('/api/function')
def function():
    return render_template('multi.html')



@app.route('/api/scatter')
def scatter():
    return render_template('scatter.html')


@app.route('/api/tc')
def tc():
    return render_template('tc.html')



if __name__ == '__main__':
    app.run()

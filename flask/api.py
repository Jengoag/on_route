## Hay que crear endpoints con cada una de las llamadas que se harán
# como las llamadas pueden ser infinitas, el endpoint se tiene que crear solo con la url que devuelva la api?? 

from os import read
from flask import Flask, request
from connection_sql import db  
from json_response import json_response
import requests

app = Flask("api")

@app.route("/")
def hello():
    return "<p>On route</p>"

## GET ADDRESSES

@app.route("/get_addresses")
def get_addresses():
    query = """
        SELECT *
        FROM routes_created
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## STORE ADDRESSES

@app.route("/store_addresses", methods = ['POST'])
def store_addresses():
        initial = request.form.get("initial")


## XY_ADRESSES_DB

@app.route("/xy_adresses_db")
def xy_parques():
    query = f"""
        SELECT name_area, latitude, longitude
        FROM parques
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

 
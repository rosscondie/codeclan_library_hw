from flask import render_template, request, redirect
import datetime 

from app import app

@app.route("/")
def index():
    return "Hello World!"
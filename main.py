
from flask import Flask, render_template,request, send_file, redirect,url_for,flash
from flask_cors import CORS, cross_origin
from Prediction_Application.pipeline.predicition_pipeline import Prediction
from Prediction_Application.pipeline.training_pipeline import Training_Pipeline
from Prediction_Application.constant import *
from Prediction_Application.logger import logging
import os
import sys
import shutil

app = Flask(__name__)
CORS(app)
app.secret_key = APP_SECRET_KEY

@app.route("/", methods =["GET"])
@cross_origin()
def home():
    return render_template("result.html")


if __name__=="__main__":
    
    port = int(os.getenv("PORT",5000))
    host = '0.0.0.0'
    app.run(host=host,port=port)
    
    
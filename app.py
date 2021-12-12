from flask import Flask, jsonify, request
import pandas as pd

#import config as cfg
import pipeline_predict as pp

app = Flask(__name__)
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe
    resultado = pp.predict(data)
    #print('El resultado es:', str(resultado))
    return jsonify({"Prediccion": int(resultado)})
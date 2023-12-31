import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import pandas as pd
import numpy as np

app = Flask(__name__)
##Load the model
bancamodel=pickle.load(open('Renewal_Model_updated.pkl','rb'))


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_json(['data'])
    result = bancamodel.predict_proba(data)
    print(result[:,1])
    return jsonify(result[:,1])
	
if __name__ == '__main__':
	app.run(debug=True)
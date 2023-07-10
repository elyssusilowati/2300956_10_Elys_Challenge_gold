import json
from flask import Flask,  jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])

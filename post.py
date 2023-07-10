import re
import pandas as pd

from flask import Flask,  jsonify
from flask import request
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger = Swagger(app,config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['POST'])
@app.route('/', methods=['POST'])
def cek():
    #Upload File
    file = request.files.getlist('data.csv')[0]
    
    #import csv ke pandas
    df = pd.read_csv('data.csv', encoding='latin-1')
    
    #Membuat format list
    texts = df.text.tolist()
    
    #Melakukan Cleansing Text
    cleaned_text = []
    
    for text in texts:
        cleaned_text.append(re.sub(r'[^a-zA-Z0-9]',' ',text))
        
    json_response = {
        'status_code' : 200,
        'description' : "Teks sedang Di Proses",
        'data' : cleaned_text,
    }
    
    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
    app.run()

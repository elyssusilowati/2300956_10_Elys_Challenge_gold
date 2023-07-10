import re 
import pandas as pd 
import json
import sqlite3

from flask import Flask, jsonify, request, send_file
from flasgger import Swagger, LazyString, LazyJSONEncoder 
from flasgger import swag_from 

# df1 = pd.read_csv('new_kamusalay.csv')
# dict1 = df1.to_dict('list') 
# df2 = pd.read_csv('abusive.csv')
# dict2 = df2.to_dict('list')

app = Flask(__name__) 

swagger_config = { 
    "headers": [], 
    "specs": [ { "endpoint": 'docs', 
                 "route": '/docs.json'} ],
    "static_url_path": "/flasgger_static", 
    "swagger_ui": True, 
    "specs_route": "/docs/" 
} 
swagger = Swagger(app, config=swagger_config) 

def create_json_response(description, data):
    return {
        "status code": 200,
        "description": description,
        "data": data
    }
    
def sql_database():
    conn = sqlite3.connect("databasetweet.db")
    conn.execute("CREATE TABLE if not exists tweet(text VARCHAR)")
    conn.execute("INSERT INTO tweet VALUES (?)",(json.dumps(dict),))
    conn.commit()
    conn.close()
 
@swag_from("docs/hello_world.yml", methods=['POST']) 
@app.route('/', methods=['POST']) 
def sql_database(): 
    conn = sqlite3.connect('databasetweet.db')
    conn.execute("SELECT * FROM tweet")
    conn.commit()
    conn.close()

# @swag_from("docs/text_processing.yml", methods=['POST']) 
# @app.route('/text-processing', methods=['POST']) 
# def text_processing():
#     text = request.args.get('text')
#     text = re.sub(r'[^a-zA-Z0-9!.\s]', ' ', text)
#     for typo, rev, abusive in zip(dict1['KATA'], dict1['REVISI'], dict2['ABUSIVE']):
#             text  = re.sub(r'\b{}\b'.format(typo), rev, text)
#             text  = re.sub(r'\b{}\b'.format(abusive), '', text)
#     json_response = create_json_response (description="text yang sudah di proses",data=text)
 
#     response_data = jsonify(json_response) 
#     return response_data

# @swag_from("docs/data_cleansing.yml", methods=['POST']) 
# @app.route('/data-cleansing', methods=['POST'])
# def data_cleansing():

#     file = request.files.getlist('file')[0]
#     if file and file.filename.endswith('.csv'):
#         df = pd.read_csv(file)
#         for typo, rev, abusive in zip(dict1['KATA'], dict1['REVISI'], dict2['ABUSIVE']):
#             df['Tweet'] = df['Tweet'].str.replace(r'\b{}\b'.format(typo), rev, regex=True)
#             df['Tweet'] = df['Tweet'].str.replace(r'\b{}\b'.format(abusive), '', regex=True)
#             dict = df.to_dict(orient='records')
#     json_response = create_json_response (description="Hasil file yang telah di bersihkan", data=dict)
#     response_data = jsonify(json_response)
#     return response_data
    
if __name__ == '__main__':
    app.run()
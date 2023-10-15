from flask_cors import CORS
from flask import Flask
from flask import request, jsonify
import sys

from algorithm import algo

api = Flask(__name__)
CORS(api)

counter = 0
@api.route('/algorithm')
def my_profile():
    global counter
    response_body = algo.hi(counter)
    counter += 1
    return response_body

@api.route('/algorithmSend', methods=['POST'])
def receive_data():
    if request.method == "POST":
        data = request.json
        data = data.get('data')
        print(type(data), flush=True)
        classname = data[0]
        testdate = data[1]
        return algo.hi(classname, testdate)
        
            

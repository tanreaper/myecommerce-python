from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type' 

@app.route("/")
def hello_world():
    return "<p>Welcome to authentication api!!</p>"

@app.route("/login", methods=['GET', 'POST'])
# @cross_origin()
def login():
    if request.method == 'POST':
        request.form.get('username')
        request.form.get('password')
        return jsonify({'status': "post success"})
    else:
         return jsonify({'status': "get success"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
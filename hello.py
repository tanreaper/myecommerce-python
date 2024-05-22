from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' 
app.config['MYSQL_HOST'] = 'mysql-db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'kvsp_paul'

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Welcome to authentication api!!</p>"

@app.route("/signup", methods=['GET', 'POST'])
@cross_origin()
def signup():
    if request.method == 'POST':
        username = request.json.get('name')
        email = request.json.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO pygo (name, email) VALUES (%s,%s)", (username,email))
        mysql.connection.commit()
        cursor.close()
        print(username)
        print(email)
        return jsonify({'status': "post success"})
    else:
         return jsonify({'status': "get success"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
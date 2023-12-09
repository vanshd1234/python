from flask import Flask, jsonify, request
from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
db = client['traveller']


app = Flask(__name__)

#mongo connection


@app.route("/")
def hello():
    return "hello world"

# Define a route to handle POST requests
@app.route('/register', methods=['POST'])
def add_data():
    collection = db['register']
    data = request.json
    register_data = {
        "first_name" : data["first_name"],
        "last_name" : data["last_name"],
        "email" : data["email"],
        "password" : data["password"],
        "phone_number" : data["phone_number"]
    }
    collection.insert_one(register_data)

    return jsonify({'message': 'Register Successfully', 'data': data}), 201


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from pymongo import MongoClient


app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'
# jwt = JWTManager(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
collection = db['users']
@app.route("/")
def home_page():
    return "hi khvkufktfh,!"

@app.route('/createData', methods=['POST'])
def add_data():
    # new_data = request.get_json()
    new_data = {
    "name":"archana",
    "email":"abs@gmail.com"}
    collection.insert_one(new_data)
    return jsonify({'message': 'Data added successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

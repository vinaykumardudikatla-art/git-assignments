import datetime

from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.server_api import ServerApi

app = Flask(__name__)
# Load environment variables from .env file
load_dotenv()
# MongoDB connection string from environment variable
uri = os.getenv('MONGO_URI')

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['test']
collection = db['test_collection']

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Unable to connect to the server: {e}") 

@app.route('/getdata', methods=['GET'])
def get_data():
    # Fetch data from MongoDB collection and return as JSON
    try:    
        data = list(collection.find({}, {'_id': 0}))  # Exclude the '_id' field from the results
        print("Data fetched successfully from MongoDB.")
        return jsonify(data), 200
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({'message': 'Error fetching data'}), 500

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    #include regitration date in user_data
    user_data['registration_date'] = datetime.datetime.now().isoformat()
    # Insert user data into MongoDB
    collection.insert_one(user_data)
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
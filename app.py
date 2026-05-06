from flask import Flask, jsonify, request
import pymongo
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["mycollection"]
@app.route('/get_data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))  # Exclude the _id field
    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        itemName = request.json.get('name')
        itemDescription = request.json.get('description')
        new_data = {
            "name": itemName,
            "description": itemDescription
        }
        if not new_data:
            return jsonify({"error": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    collection.insert_one(new_data)
    return jsonify({"message": "Todo item submitted successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
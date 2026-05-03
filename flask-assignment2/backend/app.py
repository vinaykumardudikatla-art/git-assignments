from flask import Flask, render_template, request # type: ignore
from pymongo.mongo_client import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import json
import datetime

current_date = datetime.datetime.now()

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

uri = MONGO_URI

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

collection = client['test']['test_collection']


app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():

    try:

        name = request.form['username']
        password = request.form['password']

        print(f"Received form data: {name}, {password}")

        existing_user = collection.find_one({"name": name})

        if existing_user:
            print(f"User {name} already exists.")
            return 'User already exists.'

        collection.insert_one({
            "name": name,
            "password": password,
            "registration_date": current_date
        })

        print(f"Submitted form data into database: {name}, {password}")

        # Handle registration logic here
        return 'Data submitted successfully!'
    except Exception as e:
        print(e)
        return 'An error occurred while submitting data.'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
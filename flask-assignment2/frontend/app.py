from flask import Flask, render_template, request # type: ignore
import requests # type: ignore
import datetime

BACKEND_URL = "http://localhost:5000"

current_date = datetime.datetime.now()

app = Flask(__name__)


@app.route('/')
def home():
    print ("Home page accessed!")

    return render_template('index.html', current_date=current_date.strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/register', methods=['POST'])
def register():

    name = request.form['username']
    password = request.form['password']
    print(f"Received form data: {name}, {password}")

    response = requests.post(f"{BACKEND_URL}/register", data={'username': name, 'password': password})
    if response.text == 'User already exists.':
          return 'User already exists.'
    else:
          return 'Data submitted successfully!'
    
@app.route('/getdata')
def get_data():
    response = requests.get(f"{BACKEND_URL}/getdata")
    if response.status_code == 200:
        data = response.json()
        print("Data received from backend:", data)
        return render_template('data.html', data=data)
    else:
        print("Failed to fetch data from backend. Status code:", response.status_code)
        return 'Failed to fetch data from backend.'


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
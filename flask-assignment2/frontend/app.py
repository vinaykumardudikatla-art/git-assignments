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


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
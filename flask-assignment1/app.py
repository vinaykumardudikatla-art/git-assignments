from flask import Flask

app = Flask(__name__) 

@app.route('/')
def home():
    return 'Hello, World! Welcome to my Flask app. <br>This is a simple example to demonstrate how to create a basic web application using Flask.' \
    '<br> /about - Learn more about this application. <br> /api - Get sample data in JSON format which reads the json file in the project folder location.'    
@app.route('/about')
def about():
    return 'This is the about page. Here you can provide information about your application, its purpose, and any other relevant details. You can also include links to your social media profiles or contact information.'

@app.route('/api')
def api():
    file = open('sampledata.json', 'r')
    data = file.read()
    file.close()
    return data

if __name__ == '__main__':
    app.run(debug=True)
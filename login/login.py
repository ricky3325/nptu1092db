from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  username = input()
  return '%r:Web App with Python Flask!' % username

app.run(host='0.0.0.0', port=5002)
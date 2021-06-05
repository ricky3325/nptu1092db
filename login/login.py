from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
  # retrive post body
  jsonobj = request.get_json(silent=True)
  username = json.dumps(jsonobj['username']).replace("\"", "")
  password = json.dumps(jsonobj['password']).replace("\"", "")

  Dmessage = dict()
  Dmessage['username'] = username
  Dmessage['password'] = password

  Dmessage = json.dumps(Dmessage)


  return ' %r :Web App with Python Flask!' % Dmessage

app.run(host='0.0.0.0', port=5002)
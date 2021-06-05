from flask import Flask, request, jsonify, json
import pymongo

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

  myclient = pymongo.MongoClient('mongodb://%s:%s/' % (
        'rs1',    # database addr
        '27041'         # database port
    ))
  mydb = myclient["UserList"]
  mycol = mydb["User"]


  x = mycol.find({'username':username, 'password': password})
  if x.count() == 1:
    return "Done"
  else:
    return "False"
  

  #return ' %r :Web App with Python Flask!' % x

app.run(host='0.0.0.0', port=5002)
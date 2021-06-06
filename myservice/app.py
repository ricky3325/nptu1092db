from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pymongo

myclient = pymongo.MongoClient('mongodb://%s:%s/' % (
        'rs3',    # database addr
        '27043'         # database port
    ))
mydb = myclient["Content"]
mycol = mydb["Info"]

# setup flask app
app = Flask(__name__)
@app.route('/')
@app.route('/readInfo', methods=['GET'])
def readInfo():
    x = mycol.find()
    if x:
      return render_template('home.html',data = x)
    else:
      return 'not found'

@app.route('/editInfo', methods=['GET'])
def editInfo():
    
    x = mycol.find()
    if x:
      return render_template('home.html',data = x)
    else:
      return 'not found'


@app.route('/deleteInfo', methods=['GET'])
def deleteInfo():
    return "deleteInfo"

@app.route('/addInfo', methods=['GET'])
def addInfo():
    return '''
    <form method="post">
     Title   <input name="title" type="text" /><br/>
     Content <input name="content" type="text" /><br/>
     <input value="Send" type="submit" />
    </form>'''

@app.route('/addInfo', methods=['POST'])
def Do_addInfo():
    title = request.form["title"]
    content = request.form["content"]

    
    x = mycol.insert_one({"title":title, "content":content})
    return render_template('home.html' ,title = title, content = content)

app.run(host='0.0.0.0', port=5003)
from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pymongo

myclient = pymongo.MongoClient('mongodb://%s:%s/' % (
        'rs1',    # database addr
        '27041'         # database port
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
      return render_template('editpage.html',data = x)
    else:
      return 'not found'

@app.route('/editInfo', methods=['POST'])
def Do_editInfo():
    title = request.form["title"]
    content = request.form["content"]
    x = mycol.update({"title":title},{"$set":{"content":content}})
    return render_template('home.html' ,title = title, content = content)


@app.route('/deleteInfo', methods=['GET'])
def deleteInfo():
    x = mycol.find()
    if x:
      return render_template('deletepage.html',data = x)
    else:
      return 'not found'

@app.route('/deleteInfo', methods=['POST'])
def Do_deleteInfo():
    title = request.form["title"]
    content = request.form["content"]
    #x = mycol.update({"title":title},{"$set":{"content":content}})
    #x = mycol.insert_one({"title":title, "content":content})
    x = mycol.delete_one({"title":title})
    return render_template('home.html' ,title = title, content = content)

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
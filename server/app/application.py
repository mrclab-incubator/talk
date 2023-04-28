from flask import Flask, render_template, request, make_response
import os
from message_manager import MessageManager
import json

dburl = "mongodb://localhost:27017/"
db = "flask_tutorial"
messageManager = MessageManager(dburl, db)

app = Flask(__name__)


@app.route("/mark1")
def hello_world():
    print(os.getcwd())
    return render_template('index_mark1.html', user="shreejit")


@app.route("/")
def default():
    return render_template('index.html')


@app.route("/messenger/send", methods=['POST'])
def send_message():
    message = request.json
    messageManager.saveMessage(message['from'], message['to'], message['message'])
    response = {
        "status": "ok"
    }
    return response


@app.route("/messenger/fetch/<user>", methods=['GET'])
def fetch_messages(user):
    messages = json.loads(json.dumps(messageManager.fetchUnread(user), default=str))
    response = {
        "status": "ok",
        "messages": messages
    }
    return response


app.run()

from dotenv import load_dotenv; load_dotenv(); # Load .env in debug mode
from flask import Flask, render_template
from utils.db import db
from utils.socket import socket
from os import getenv
from utils.blueprints import bps
from models import *

DEBUG = str(getenv("DEBUG"))
DEBUG = True if DEBUG.upper() in ('TRUE', 'YES' ) else False
HOST = getenv("HOST", '0.0.0.0')
PORT = getenv("PORT", 5000)
DB_URI = getenv("DB_URI")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

socket.init_app(app=app)
db.init_app(app)

with app.app_context(): db.create_all()

for bp in bps:  app.register_blueprint(bp, url_prefix=bps[bp])

@app.route("/")
def home():  return render_template("index.html")

if __name__ == '__main__':
    socket.run(
        app=app,
        debug=DEBUG, 
        host=HOST, 
        port=PORT
    )
